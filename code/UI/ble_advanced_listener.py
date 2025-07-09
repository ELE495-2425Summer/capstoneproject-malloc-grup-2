from bleak import BleakScanner, BleakClient
import asyncio
from multiprocessing import Queue
import time
from datetime import datetime
import threading

# Global message queue (process-safe)
message_queue = Queue()


class BLEListener:
    def __init__(self):
        self._running = False
        self._connection_status = "disconnected"
        self._last_error = None
        self._client = None
        self._callback = None

    async def _listen(self):
        while self._running:
            try:
                self._connection_status = "scanning"
                print("\n🔍 RPi aranıyor...")
                device = await BleakScanner.find_device_by_name("RPi_BLE", timeout=10)

                if not device:
                    self._connection_status = "device_not_found"
                    print("❌ Cihaz bulunamadı. 5 saniye sonra tekrar denenecek...")
                    await asyncio.sleep(5)
                    continue

                self._connection_status = "connecting"
                self._client = BleakClient(device)
                await self._client.connect()
                self._connection_status = "connected"
                print(f"✅ Bağlantı kuruldu: {device.address}")

                def callback(sender, data):
                    message_queue.put({
                        "timestamp": datetime.now().isoformat(),
                        "message": data.decode(),
                        "status": "received"
                    })

                await self._client.start_notify("0000FFE1-0000-1000-8000-00805F9B34FB", callback)

                # Bağlantı aktifken bekle
                while self._running and self._client.is_connected:
                    await asyncio.sleep(1)

            except Exception as e:
                self._connection_status = "error"
                self._last_error = str(e)
                print(f"⚠️ Hata: {str(e)}. Yeniden bağlanılıyor...")
                await self._safe_disconnect()
                await asyncio.sleep(5)

    async def _safe_disconnect(self):
        if self._client and self._client.is_connected:
            await self._client.disconnect()

    def start(self):
        if not self._running:
            self._running = True
            threading.Thread(
                target=lambda: asyncio.run(self._listen()),
                daemon=True
            ).start()
            print("BLE dinleyici başlatıldı")

    def stop(self):
        self._running = False
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._safe_disconnect())
        loop.close()
        print("BLE dinleyici durduruldu")

    def get_status(self):
        return {
            "status": self._connection_status,
            "last_error": self._last_error,
            "queue_size": message_queue.qsize()
        }


# Singleton instance
listener = BLEListener()


def get_message():
    """Son mesajı al (non-blocking)"""
    try:
        return message_queue.get_nowait()
    except:
        return None