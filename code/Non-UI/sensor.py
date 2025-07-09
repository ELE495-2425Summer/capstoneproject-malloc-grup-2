import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG=13
ECHO=26
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT)

# def mesafe_hesap():
#     
#     GPIO.setmode(GPIO.BCM)
#     trig=13
#     echo=26
#     GPIO.setup(echo,GPIO.IN)
#     GPIO.setup(trig,GPIO.OUT)    
#     GPIO.output(trig,True)
#     time.sleep(0.0001)
#     GPIO.output(trig,False)
#     while GPIO.input (echo) == 0:
#         pulse_start = time.time()
#     while GPIO.input(echo) ==1:
#         pulse_end = time.time()
#     pulse_duration = pulse_end - pulse_start
#     distance = (pulse_duration*34000)/2
#     dist= round(distance,2)
#     return dist
def mesafe_hesap():
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = None
    pulse_end = None

    timeout = time.time() + 0.04
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if time.time() > timeout:
            return -1  # zaman aşımı

    timeout = time.time() + 0.04
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if time.time() > timeout:
            return -1

    # Bu kontrol hatayı engeller
    if pulse_start is None or pulse_end is None:
        return -1

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if distance < 1 or distance > 400:
        return -1

    return distance


# while True:
#     print(mesafe_hesap())
#     time.sleep(0.001)
    