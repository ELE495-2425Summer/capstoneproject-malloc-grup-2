import RPi.GPIO as GPIO
import time
IN1 = 17
IN2 = 4
ENA = 25
IN3 = 22
IN4 = 23
ENB = 24
GPIO.setmode(GPIO.BCM)

motor_pins = [IN1, IN2, ENA, IN3, IN4, ENB]
# for pin in motor_pins:
#     GPIO.setup(pin, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
# PWM tanımla
pwmA = GPIO.PWM(ENA, 1000)  # 1 kHz
pwmB = GPIO.PWM(ENB, 1000)

pwmA.start(0)
pwmB.start(0)

def motorA_forward(speed=70):
    
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwmA.ChangeDutyCycle(speed)


def motorA_backward(speed=70):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwmA.ChangeDutyCycle(speed)

def motorB_backward(speed=70):
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwmB.ChangeDutyCycle(speed)

def motorB_forward(speed=70):
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwmB.ChangeDutyCycle(speed)

def stop_all():
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# x = 40
# try:
# #     time.sleep(10)
#     print("Motorlar ileri gidiyor...")
#     motorA_forward(speed=x)
#     motorB_forward(speed=x)
#     time.sleep(5)
#     
#     time.sleep(0.2)
#     stop_all()
#     print("Motorlar geri gidiyor...")
#     motorA_backward(speed=x)
#     motorB_backward(speed=x)
#     time.sleep(5)
#     print("Motorlar sağ gidiyor...")
#     stop_all()
#     time.sleep(0.2)
#     motorB_forward(speed=x)
#     motorA_backward(speed=x)
#     time.sleep(5)
#     stop_all()
#     time.sleep(10)
#     print("Motorlar ileri gidiyor...")
#     motorA_forward(speed=x)
#     motorB_forward(speed=x)
#     time.sleep(5)
#     
#     time.sleep(0.2)
#     stop_all()
#     print("Motorlar geri gidiyor...")
#     motorA_backward(speed=x)
#     motorB_backward(speed=x)
#     time.sleep(5)
#     print("Motorlar sağ gidiyor...")
#     stop_all()
#     time.sleep(0.2)
#     motorB_forward(speed=x)
#     motorA_backward(speed=x)
#     time.sleep(5)
#     print("Durdu")
#     stop_all()
# finally:
#     GPIO.cleanup()
# 
