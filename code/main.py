from stt_modulu import stt_kaydi_baslat, stt_kaydi_durdur_ve_coz, stt_loop
from tts_modulu import metni_sese_cevir_ve_oku
import threading
import time
from pydub import AudioSegment
from pydub.playback import play
from LLM import ask_chatgpt
from Rpi_sender import BluetoothClient
import json
from motorobit import motorA_backward, motorA_forward, motorB_backward, motorB_backward
from komut_isleyici import yorumla_ve_uygula
import RPi.GPIO as GPIO

# -11,-6,-7 olduğu zaman baştan başlatma kodu koy
Button_pin = 11
led_pin = 5


def anakod():
    GPIO.setmode(GPIO.BCM)
    print('oley')   
    stt_kaydi_baslat()
    threading.Thread(target=stt_loop).start()

    #time.sleep(5)
def anakod2(client):
    
    try:
        
        metin,verified = stt_kaydi_durdur_ve_coz()
        print(f"verified: {verified}")
        if verified or True:
            komutlar = ask_chatgpt(metin, model="gpt-4o")
            anlik = "anlik"
            bilgiler = {'alinan_ses': metin,'komutlar': komutlar, 'anlik': anlik}
            bilgi_str = json.dumps(bilgiler)
            
            client.gonder(bilgi_str)

            yorumla_ve_uygula(komutlar,bilgiler,client)
        else:
            print("tanınamayan kullanıcı")
    except Exception as e:
        print("STT sırasında hata olustu:",e)
        metin = ""
    
    
def buton_durumunu_oku():
    try:
        with open("/home/aamir/Desktop/moduller/buton_flag.txt", "r") as f:
            return f.read().strip() == "1"
        
    except:
        return False
 
def main():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(led_pin, GPIO.OUT)
        client = BluetoothClient("14:85:7F:7D:A5:36")
        client.connect()
        try:
            while True:
                print(f"bekliyorruuum... \n buton durumu: {GPIO.input(Button_pin)} \n arayuzden {buton_durumunu_oku()}")
                GPIO.output(led_pin,True)
                if GPIO.input(Button_pin) == GPIO.HIGH or buton_durumunu_oku():
                    print(buton_durumunu_oku())
                    GPIO.output(led_pin,False)
                    anakod()
                    while GPIO.input(Button_pin) == GPIO.HIGH or buton_durumunu_oku():
                        pass
                    anakod2(client)
                    time.sleep(0.5)
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("program sonlandırıldı.")
            GPIO.output(led_pin,False)
        finally:
            GPIO.output(led_pin,False)
            GPIO.cleanup()
            
if __name__ == "__main__":
    main()
