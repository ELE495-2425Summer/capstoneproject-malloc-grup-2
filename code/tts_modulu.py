from google.cloud import texttospeech
from google.oauth2.service_account import Credentials
import os


# Google Cloud kimlik dosyası (.json)
GOOGLE_CLOUD_KEY = "path/to/your-json-file"
credentials = Credentials.from_service_account_file(GOOGLE_CLOUD_KEY)
tts_client = texttospeech.TextToSpeechClient(credentials=credentials)



# Metni seslendirme
def metni_sese_cevir_ve_oku(metin, dosya="cevap.mp3"):
    # 1. Metni API'ye gönderilecek yapıya hazırlama
    synthesis_input = texttospeech.SynthesisInput(text=metin)

    # 2. Türkçe doğal ses seçimi
    voice = texttospeech.VoiceSelectionParams(
        language_code="tr-TR",           # Türkçe dil kodu
        name="tr-TR-Wavenet-A"           # Doğal (Wavenet) ses
    )

    # 3. Çıkış formatı (MP3)
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # 4. API isteği gönder
    response = tts_client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # 5. Ses dosyasını çal (sisteme göre değişir)
    try:
        # Raspberry Pi veya Linux için
        with open(dosya,"wb") as out:
            out.write(response.audio_content)
        os.system(f"ffplay -nodisp -autoexit {dosya}")
        
    except:
        # Windows için alternatif (varsayılan medya oynatıcıyla açar)
        os.system(f"mpeg321 {dosya}")


    
