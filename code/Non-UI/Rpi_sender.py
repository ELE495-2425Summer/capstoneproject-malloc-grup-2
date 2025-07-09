import bluetooth
import threading
import queue
import time

class BluetoothClient:
    def __init__(self, mac_adresi, port=5):
        self.mac_adresi= mac_adresi
        self.port= port
        self.sock= None
        self.send_queue = queue.Queue()
        self.running= False
        
    def connect(self):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((self.mac_adresi, self.port))
        print("baglantı kuruldu")
        self.running = True
        threading.Thread(target=self.sender_loop, daemon=True).start()
        
    def sender_loop(self):
        while self.running:
            try:
                mesaj= self.send_queue.get(timeout=1)
                self.sock.send(mesaj)
                print(f"gönderildi: {mesaj}")
            except queue.Empty:
                continue
            except Exception as e:
                print("gonderme hatası:",e)
                self.running = False
                break
    def gonder(self,mesaj):
        self.send_queue.put(mesaj)
    def kapat(self):
        self.running = False
        if self.sock:
            self.sock.close()
            print("bağlantı kapatıldı")
            
