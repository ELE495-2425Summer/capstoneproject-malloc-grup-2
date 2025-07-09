import re
import time
from motorobit import motorA_forward, motorA_backward, motorB_forward, motorB_backward, stop_all
from tts_modulu import metni_sese_cevir_ve_oku
from sensor import mesafe_hesap
from gyro2 import gyro_ile_donus
import json

komutlar = "[sağa dön]"
def yorumla_ve_uygula(komut_stringi,bilgiler,client):
    komutlar = re.findall(r'\[([^\[\]]+)\]', komut_stringi)
    
    for komut in komutlar:
        komut = komut.lower()
        
        ########buraya bakılacak#######
        sure_eslesme = re.search(r'(\d+)\s*saniye', komut)
        sure = int(sure_eslesme.group(1)) if sure_eslesme else 15
        
        
        if "ileri" in komut:
            metni_sese_cevir_ve_oku(f"{sure} saniye İleri gidiyorum")
            bilgiler['anlik']="ileri gidiyorum"
            bilgi_str = json.dumps(bilgiler)
            
            client.gonder(bilgi_str)
            
            baslangic = time.time()
            motorA_forward()
            motorB_forward()
            while time.time() - baslangic < sure:  
                mesafe = mesafe_hesap()
                    
                print('mesafe',mesafe,'cm')
                    
                if 0< mesafe < 20 :
                    break
                time.sleep(0.001)
            stop_all()

        elif "sola" in komut:
            metni_sese_cevir_ve_oku("Sola dönüyorum")
            bilgiler['anlik']="sola dönüyorum"
            bilgi_str = json.dumps(bilgiler)
            
            client.gonder(bilgi_str)
            
            
            
            motorA_forward()
            motorB_backward()
            #gyro_ile_donus(90, carpan = 1)
            time.sleep(0.8)
            stop_all()

        elif "sağa" in komut:
            metni_sese_cevir_ve_oku("Sağa dönüyorum")
            bilgiler['anlik']="sağa dönüyorum"
            bilgi_str = json.dumps(bilgiler)
            
            client.gonder(bilgi_str)
            motorB_forward()
            motorA_backward()
            #gyro_ile_donus(90, carpan = 1)
            time.sleep(0.8)
            stop_all()

        elif "dur" in komut:
            metni_sese_cevir_ve_oku(f"{sure} Saniye Duruyorum")
            bilgiler['anlik']="duruyorum"
            bilgi_str = json.dumps(bilgiler)
            
            client.gonder(bilgi_str)
            stop_all()
            time.sleep(sure)
        elif "geri" in komut:
            if 'dön' in komut:
                metni_sese_cevir_ve_oku("geri dönüyorum")
                bilgiler['anlik']="geri dönüyorum"
                bilgi_str = json.dumps(bilgiler)
                client.gonder(bilgi_str)
                motorA_forward()
                motorB_backward()
                #gyro_ile_donus(180, carpan = -1)
                time.sleep(1.3)
                stop_all()
            else:
                metni_sese_cevir_ve_oku(f"geri dönüyorum ve {sure} saniye ileri gidiyorum")
                bilgiler['anlik']="geri dönüyorum ve ileri gidiyorum"
                bilgi_str = json.dumps(bilgiler)
            
                client.gonder(bilgi_str)
                
                
                motorA_forward()
                motorB_backward()
                #gyro_ile_donus(180, carpan = -1)
                time.sleep(1.3)
                baslangic = time.time()
                motorA_forward()
                motorB_forward()
                while time.time() - baslangic < sure:  
                    mesafe = mesafe_hesap()
                    
                    print('mesafe',mesafe,'cm')
                    
                    if 0<mesafe < 20 :
                        break
                    time.sleep(0.001)
                stop_all()

        else:
            metni_sese_cevir_ve_oku(f"Anlaşılamayan komut: {komut}")
            bilgiler['anlik']="Anlamadım"
            bilgi_str = json.dumps(bilgiler)
            
            client.gonder(bilgi_str)
# if __name__ == "__main__":
    #while True:
        #x = float(input("zart: "))
        
        #motorA_forward(speed=60)
        #motorB_backward(speed=60)
        #time.sleep(x)
        #stop_all()
