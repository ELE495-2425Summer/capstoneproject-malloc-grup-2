import time
from PyQt5.QtCore import QIODevice, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QDockWidget, QLabel, QMessageBox, QWidget
import sys
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui, QtCore
from PyQt5.QtSerialPort import QSerialPort
from MainWindow import Ui_MainWindow
from datetime import datetime
import json
from ble_thread import BluetoothListenerThread
import csv
import random
import string
import threading
import os
import paramiko
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Python311\Lib\site-packages\PyQt5\Qt5\plugins'


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.car_state = True  # Başlangıçta ikon durumu
        self.mic_state = True

        # Başlangıçta zamanı ayarla
        self.ui.Tarih.setText(self.guncel_zaman())

        # Zamanı güncellemek için timer oluştur
        self.timer = QTimer()
        self.timer.timeout.connect(self.guncel_zaman_goster)
        self.timer.start(1000)  # Her 1 saniyede bir güncelle

        # Buton tıklama sinyali bağlanıyor
        self.ui.StartCar_Button.clicked.connect(self.start_car)
        self.ui.StartMic_Button.clicked.connect(self.start_mic)

        # BLE Thread'i başlat
        self.ble_thread = BluetoothListenerThread()
        self.ble_thread.new_message.connect(self.handle_ble_message)
        self.ble_thread.status_updated.connect(self.handle_status_update)
        self.ble_thread.connection_changed.connect(self.handle_connection_change)
        self.bitirilenKomut = []


        self.connection_icons = {
            "disconnected": ":/disconnected.png",
            "scanning": ":/searching.png",
            "connected": ":/connected.png",
            "error": ":/error.png"
        }
        self.ble_thread.start()

    def handle_ble_message(self, msg):
        print("BLE MESSAGE:", msg)
        self.ble_gelen_mesaj = json.loads(msg)
        ham_komutlar = self.ble_gelen_mesaj["komutlar"]
        self.liste = [komut.strip() for komut in ham_komutlar.split(",")]
        metin = ",\n".join(self.liste) + "\n"
        self.ui.textEdit_2.setPlainText(metin)
        self.ui.label.setText(self.ble_gelen_mesaj['alinan_ses'])
        self.ui.Komut_bilgisi.setText(self.ble_gelen_mesaj['anlik'])
        self.kalanlarlist = self.liste[:]
        for emir in self.kalanlarlist[:]:
            flag1=0
            if self.ble_gelen_mesaj['anlik'] in emir:
                #self.liste.remove(emir)
                #metin2 = ",\n".join(self.liste) + "\n"
                #self.ui.textEdit_2.setPlainText(metin2)
                self.bitirilenKomut.append(emir)
                bitirilen = ",\n".join(self.bitirilenKomut) + "\n"
                self.ui.textEdit.setPlainText(bitirilen)
                for kalan in self.bitirilenKomut:
                    if kalan in self.liste:
                        self.kalanlarlist.remove(kalan)
                        metin2 = ",\n".join(self.kalanlarlist) + "\n"
                        self.ui.textEdit_2.setPlainText(metin2)
                        flag1=1
                if flag1:
                    break
        if self.bitirilenKomut == self.liste:
            self.bitirilenKomut.append("------------------------------\n")
            self.ui.textEdit.setPlainText(self.bitirilenKomut)

    def handle_status_update(self, status):
        self.ui.Bluetooth_durum_3.setText(
            f"{status['status']} | Hata: {status['last_error'] or 'Yok'}"
        )

    def handle_connection_change(self, status):
        pixmap = QtGui.QPixmap(self.connection_icons.get(status, ":/disconnected.png"))
        scaled_pixmap = pixmap.scaled(25, 25, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.Bluetooth_durum_2.setPixmap(scaled_pixmap)
        self.ui.Bluetooth_durum_2.setToolTip(f"BLE: {status}")

    def closeEvent(self, event):
        """Pencere kapanırken temizlik"""
        if self.ble_thread.isRunning():
            self.ble_thread.stop()
        event.accept()

    def start_car(self):
        if self.car_state:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/simge/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.StartCar_Button.setIcon(icon)
            self.ui.StartCar_Button.setIconSize(QtCore.QSize(50, 50))
            self.ui.StartCar_Button.setStyleSheet("QPushButton {\n"
                                                  "    background-color: #d90d0d;\n"
                                                  "    border-radius: 25%;\n"
                                                  "    min-width: 10px;\n"
                                                  "    min-height: 10px;\n"
                                                  "}")
            self.ui.label_2.setText("Araç Çalışır Durumda")
            self.rpi_kodu_calistir()

        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/simge/restart.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.ui.StartCar_Button.setIcon(icon)
            self.ui.StartCar_Button.setIconSize(QtCore.QSize(30, 30))
            self.ui.StartCar_Button.setStyleSheet("QPushButton {\n"
                                                  "    background-color: #35bd0f;\n"
                                                  "    border-radius: 25%;\n"
                                                  "    min-width: 10px;\n"
                                                  "    min-height: 10px;\n"
                                                  "}")
            self.ui.label_2.setText("Araç gücü kapatıldı.")
            self.rpi_kodu_durdur()


            # Durumu tersine çevir
        self.car_state = not self.car_state

    def start_mic(self):
        if self.mic_state:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/simge/micstop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.StartMic_Button.setIcon(icon)
            self.ui.StartMic_Button.setIconSize(QtCore.QSize(30, 30))
            self.ui.StartMic_Button.setStyleSheet("QPushButton {\n"
                                                  "    background-color: #d90d0d;\n"
                                                  "    border-radius: 25%;\n"
                                                  "    min-width: 10px;\n"
                                                  "    min-height: 10px;\n"
                                                  "}")
            self.buton_flag_yaz(1)

        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/simge/mic_111082.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.StartMic_Button.setIcon(icon)
            self.ui.StartMic_Button.setIconSize(QtCore.QSize(30, 30))
            self.ui.StartMic_Button.setStyleSheet("QPushButton {\n"
                                                  "    background-color: #35bd0f;\n"
                                                  "    border-radius: 25%;\n"
                                                  "    min-width: 10px;\n"
                                                  "    min-height: 10px;\n"
                                                  "}")
            self.buton_flag_yaz(0)

            # Durumu tersine çevir
        self.mic_state = not self.mic_state

    def rpi_kodu_calistir(self):
        host = "10.2.144.147" #"10.2.137.118"         #"192.168.0.11"#ev #"10.2.137.118" #okul  # RPi IP adresi
        username = "aamir"  # RPi kullanıcı adı
        password = "raspberry"  # RPi şifresi
        komut = "/home/aamir/Desktop/venv31/bin/python3 /home/aamir/Desktop/moduller/main.py"  # RPi'de çalıştırılacak dosya

        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=username, password=password)

            stdin, stdout, stderr = client.exec_command(komut)
            print("✅ Kod başlatıldı!")
            client.close()

            # Arayüzde bilgi mesajı göster
            QMessageBox.information(None, "Başarı", "RPi kodu yeniden başlatıldı.")

        except Exception as e:
            print("❌ Bağlantı hatası:", e)
            QMessageBox.critical(None, "Hata", f"RPi'ye bağlanılamadı:\n{str(e)}")

    def buton_flag_yaz(self,deger):
        host = "192.168.0.11" #"10.2.144.147"
        username = "aamir"
        password = "raspberry"

        komut = f"echo {int(deger)} > /home/aamir/Desktop/moduller/buton_flag.txt"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        ssh.exec_command(komut)
        ssh.close()

    def rpi_kodu_durdur(self):
        host = "10.2.144.147" #"10.2.137.118"     #"192.168.0.11"#"10.2.137.118"
        username = "aamir"
        password = "raspberry"
        komut = "^C"

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)

            ssh.exec_command(komut)
            ssh.close()

            QMessageBox.information(None, "Başarılı", "RPi'deki kod durduruldu.")
        except Exception as e:
            QMessageBox.critical(None, "HATA", f"Kodu durdururken hata oluştu:\n{str(e)}")

    def guncel_zaman_goster(self):
        """Zamanı gösteren QLabel'i günceller"""
        self.ui.Tarih.setText(self.guncel_zaman())

    def guncel_zaman(self):
        """Güncel zamanı Türkçe olarak döndürür"""
        su_an = datetime.now()

        # Türkçe ay ve gün isimleri
        aylar = [
            "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
            "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
        ]

        gunler = [
            "Pazartesi", "Salı", "Çarşamba", "Perşembe",
            "Cuma", "Cumartesi", "Pazar"
        ]

        # Tarih ve saat bilgilerini biçimlendir
        tarih = f"{su_an.day} {aylar[su_an.month - 1]} {su_an.year}"
        gun = gunler[su_an.weekday()]
        saat = su_an.strftime("%H:%M:%S")

        # Sonucu birleştir
        return f"{tarih}, {gun} - Saat: {saat}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.showMaximized()
    sys.exit(app.exec())