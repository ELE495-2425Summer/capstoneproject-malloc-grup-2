from mpu6050 import mpu6050
import time
import smbus

# MPU6050 başlat
gyro = mpu6050(0x68)

# Motor kontrol fonksiyonları (senin motor sürücüne göre değişebilir)
def sola_don():
    # sol motor geri, sağ motor ileri
    pass

def saga_don():
    # sol motor ileri, sağ motor geri
    pass

def dur():
    # iki motoru da durdur
    pass

# Açısal dönüşü hesapla
def gyro_don(angle_goal, direction='right'):
    print("Başladı...")
    dur()
    time.sleep(1)

    # Başlangıç zamanı
    last_time = time.time()
    total_angle = 0

    # Dönmeye başla
    if direction == 'right':
        saga_don()
    elif direction == 'left':
        sola_don()

    while abs(total_angle) < abs(angle_goal):
        now = time.time()
        dt = now - last_time
        last_time = now

        gyro_data = gyro.get_gyro_data()
        z = gyro_data['z']  # z ekseni genelde yatay düzlemde dönüş verir

        # Açı hesapla (derece/saniye * saniye = derece)
        total_angle += z * dt
        print(f"Toplam açı: {total_angle:.2f}")

    dur()
    print("Dönüş tamamlandı.")

# Örnek kullanım
gyro_don(90, direction='right')   # 90 derece sağa dön
gyro_don(90, direction='left')    # 90 derece sola dön
gyro_don(180, direction='right')  # 180 derece sağa (geriye) dön
