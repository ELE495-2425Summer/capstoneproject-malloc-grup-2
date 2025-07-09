# pc_ble_server.py
from bleak import BleakGATTServer
import asyncio

SERVICE_UUID = "0000FFE0-0000-1000-8000-00805F9B34FB"
CHAR_UUID = "0000FFE1-0000-1000-8000-00805F9B34FB"

async def main():
    server = BleakGATTServer()
    await server.start()
    service = server.add_service(SERVICE_UUID)
    characteristic = service.add_characteristic(CHAR_UUID, ["read", "write", "notify"])
    print(f"PC sunucusu başladı. MAC: {server.address}")
    await asyncio.Event().wait()  # Sonsuza kadar bekle

asyncio.run(main())