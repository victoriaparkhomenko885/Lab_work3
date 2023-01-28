import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

baselineTemp = 0
celsius = 0
fahrenheit = 0

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

while True:
    baselineTemp = 40
    celsius = ((analogRead(A0) - 20) * 3.04) / 1023 * 165 - 40
    fahrenheit = ((celsius * 9) / 5 + 32)
    print(celsius, "C, ", fahrenheit, "F")
    
    if celsius < baselineTemp:
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
    elif celsius >= baselineTemp and celsius < baselineTemp + 10:
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
    elif celsius >= baselineTemp + 10 and celsius < baselineTemp + 20:
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
    elif celsius >= baselineTemp + 20 and celsius < baselineTemp + 30:
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
    elif celsius >= baselineTemp + 30:
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
    time.sleep(1)

