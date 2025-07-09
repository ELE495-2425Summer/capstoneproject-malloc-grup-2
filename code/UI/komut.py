import time
import threading


x = "ileri git"  # Örnek giriş (dışarıdan gelecek)
sure = 10         # Örnek süre (dışarıdan gelecek)
flag = 0

def saga_don():
    print("saga_don")

def sola_don():
    print("sola_don")

def ileri_git():
    print("ileri_git")

def geri_git():
    print("geri_git")

def dur():
    print("dur")

def calistir():
    print("calistir")

# Fonksiyon referansları (PARANTEZSİZ!)
komutlar = {
    "ileri git": ileri_git,
    "geri git": geri_git,
    "sağa dön": saga_don,
    "sola dön": sola_don,
    "dur": dur,
    "calistir": calistir
}

fonksiyon_sureleri = {}  # {fonksiyon: sure}

# Örnek: Dışarıdan gelen x ve sure'yi ekleme
if x in komutlar:
    fonksiyon_sureleri[komutlar[x]] = sure  # Örneğin: {ileri_git: 2}

# Thread'leri başlat
def calistir_fonksiyon(fonksiyon, sure):
    baslangic = time.time()
    while time.time() - baslangic < sure:
        fonksiyon()
        time.sleep(0.1)

threads = []
for fonksiyon, sure in fonksiyon_sureleri.items():
    thread = threading.Thread(target=calistir_fonksiyon, args=(fonksiyon, sure))
    thread.start()
    threads.append(thread)

# Thread'lerin bitmesini bekle
for thread in threads:
    thread.join()

print("Tüm komutlar tamamlandı!")
