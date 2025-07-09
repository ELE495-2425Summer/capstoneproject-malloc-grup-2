# bluetooth_listener.py
import bluetooth
from PyQt5.QtCore import QThread, pyqtSignal


class BluetoothListenerThread(QThread):
    new_message = pyqtSignal(str)
    connection_changed = pyqtSignal(str)  # "connected", "disconnected"
    status_updated = pyqtSignal(dict)     # {"status": "...", "last_error": "..."}

    def __init__(self):
        super().__init__()
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            server_sock.bind(("", 5))
            server_sock.listen(1)
            self.status_updated.emit({"status": "Dinleniyor", "last_error": None})
        except Exception as e:
            self.status_updated.emit({"status": "Dinleme başlatılamadı", "last_error": str(e)})
            return

        while self._running:
            try:
                client_sock, address = server_sock.accept()
                self.connection_changed.emit("connected")
                self.status_updated.emit({"status": f"{address} bağlandı", "last_error": None})

                try:
                    while self._running:
                        data = client_sock.recv(1024)
                        if not data:
                            break
                        mesaj = data.decode("utf-8")
                        self.new_message.emit(mesaj)
                except Exception as e:
                    self.status_updated.emit({"status": "Veri alma hatası", "last_error": str(e)})
                finally:
                    client_sock.close()
                    self.connection_changed.emit("disconnected")
                    self.status_updated.emit({"status": "Bağlantı kapandı", "last_error": None})

            except Exception as e:
                self.status_updated.emit({"status": "Bağlantı hatası", "last_error": str(e)})

        server_sock.close()
        self.connection_changed.emit("disconnected")
