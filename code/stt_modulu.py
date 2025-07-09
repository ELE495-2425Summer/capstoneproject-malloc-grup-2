import pyaudio
import threading
from google.cloud import speech_v1 as speech
from google.oauth2.service_account import Credentials
import io
from pydub import AudioSegment
import os
import numpy as np
from pveagle import EagleProfiler, Eagle, EagleProfile
import RPi.GPIO as GPIO
from tts_modulu import metni_sese_cevir_ve_oku
LED = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

GOOGLE_CLOUD_KEY = "path/to/your-json-file"
credentials = Credentials.from_service_account_file(GOOGLE_CLOUD_KEY)
speech_client = speech.SpeechClient(credentials=credentials)



EAGLE_ACCESS_KEY = "Your-Eagle-Access-Key"
PROFILE_DIR = "speaker_profiles"
FORMAT = pyaudio.paInt16
CHANNELS = 1
RECORD_SECONDS = 2
FRAME_LENGTH = 512
RATE = 16000
CHUNK = int(RATE / 30)
THRESHOLD = 0.55
EAGLE_LIBRARY_PATH = "/home/aamir/Desktop/moduller/libpv_eagle.so" 
EAGLE_MODEL_PATH = "/home/aamir/Desktop/moduller/eagle_params.pv"


is_recording = False
audio_frames = []
audio_stream = None
audio_interface = pyaudio.PyAudio()

def stt_kaydi_baslat():
    global is_recording, audio_stream, audio_frames
    is_recording = True
    audio_frames = []

    audio_stream = audio_interface.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print("Kayıt başladı...")
    GPIO.output(LED, GPIO.HIGH)
    

def stt_loop():
    global is_recording, audio_stream, audio_frames

    while is_recording:
        data = audio_stream.read(CHUNK)
        audio_frames.append(data)
def enroll_speaker(name):
    profiler = EagleProfiler(access_key=EAGLE_ACCESS_KEY,
                             library_path=EAGLE_LIBRARY_PATH,
                             model_path=EAGLE_MODEL_PATH)

    percent = 0.0
    while percent < 100.0:
        audio = record_audio()
        percent, feedback = profiler.enroll(audio)
        print(f"Progress: {percent:.1f}% | Feedback: {feedback.name}")

    profile = profiler.export()
    profile_bytes = profile.to_bytes()

    os.makedirs(PROFILE_DIR, exist_ok=True)
    with open(os.path.join(PROFILE_DIR, f"{name}.pv"), "wb") as f:
        f.write(profile_bytes)

    print(f"✅ Enrolled speaker '{name}' and saved profile.")
def load_profiles():
    profiles = []
    names = []
    for filename in os.listdir(PROFILE_DIR):
        if filename.endswith(".pv"):
            with open(os.path.join(PROFILE_DIR, filename), "rb") as f:
                profile_bytes = f.read()
            profile = EagleProfile.from_bytes(profile_bytes)
            profiles.append(profile)
            names.append(os.path.splitext(filename)[0])
    return profiles, names

def verify_speaker(AUDI):
    profiles, names = load_profiles()

    if not profiles:
        print("⚠️ No enrolled profiles found.")
        return

    eagle = Eagle(
        access_key=EAGLE_ACCESS_KEY,
        library_path=EAGLE_LIBRARY_PATH,
        model_path=EAGLE_MODEL_PATH,
        speaker_profiles=profiles
    )

    audio = AUDI
    speaker_votes = {}

    num_frames = len(audio) // eagle.frame_length
    for i in range(num_frames):
        frame = audio[i * eagle.frame_length : (i + 1) * eagle.frame_length]
        scores = eagle.process(frame)  

        best_id = int(np.argmax(scores))
        best_score = scores[best_id]

        if best_score > 0.25: 
            speaker_votes[best_id] = speaker_votes.get(best_id, 0) + 1
    
    
    if speaker_votes:
        final_id = max(speaker_votes, key=speaker_votes.get)
        print(f"Verified speaker: {names[final_id]}")
#         metni_sese_cevir_ve_oku(f"Kullanıcı: {names[final_id]}")
        return True
    else:
        print("Speaker not recognized")
        metni_sese_cevir_ve_oku("Yetkilendirme başarısız")
        return False
        

def stt_kaydi_durdur_ve_coz():
    global is_recording, audio_stream, audio_frames

    is_recording = False
    print("Kayıt durduruldu.")
    GPIO.output(LED, GPIO.LOW)

    audio_stream.stop_stream()
    audio_stream.close()
    audio_data = b''.join(audio_frames)
    audio_pcm = np.frombuffer(audio_data, dtype=np.int16)
    verified = verify_speaker(audio_pcm)
    #if not verified:
    #    quit()
    
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code="tr-TR"
    )
    
    # STT API çağrısı
    response = speech_client.recognize(config=config, audio=audio)

    if response.results:
        metin = response.results[0].alternatives[0].transcript
        print("Tanınan Metin:", metin)
        return metin,verified
    else:
        print("Hiçbir şey tanınamadı.")
        return ""
