#!/usr/bin/python3

import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        tempmod=(temp.replace("temp=",""))
        return(float)(tempmod.replace("'C",""))
        
finaltemp = measure_temp()

print(finaltemp)

if finaltemp >= 75:
    GPIO.output(25, GPIO.HIGH)
else:
    GPIO.output(25, GPIO.LOW)
        
