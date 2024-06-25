import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
print("LED on")
GPIO.output(25,GPIO.HIGH)
#GPIO.output(24,GPIO.HIGH)
#PIO.output(23,GPIO.HIGH)
time.sleep(1)
print("LED off")
#GPIO.output(25,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(23,GPIO.LOW)

