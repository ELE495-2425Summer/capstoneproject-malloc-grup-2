# win_receiver_multi.py
import bluetooth
import threading

gelen_mesaj = ""

def handle_client(client_sock, address):
    global gelen_mesaj
    print(f"📲 Yeni bağlantı: {address}")
    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            gelen_mesaj = data.decode("utf-8")
            print("📩 Alındı:", gelen_mesaj)
    except Exception as e:
        print("❌ Hata:", e)
    finally:
        client_sock.close()

def bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", 5))
    server_sock.listen(1)

    print("🔊 Dinleniyor...")

    try:
        while True:
            client_sock, address = server_sock.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_sock, address), daemon=True)
            client_thread.start()
    except Exception as e:
        print("💥 Sunucu hatası:", e)
    finally:
        server_sock.close()

server_thread = threading.Thread(target=bluetooth_server, daemon=True)
server_thread.start()

# Ana program sürekli çalışsın
import time
son_mesaj = ""
while True:
    if gelen_mesaj != son_mesaj:
        print("🆕 Yeni mesaj:", gelen_mesaj)
        son_mesaj = gelen_mesaj
    time.sleep(0.5)
