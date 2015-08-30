#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
def blinkMode() :
    print('Lights on!')
    while 1 :
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        time.sleep(.5)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(27,GPIO.LOW)
        time.sleep(.5)
blinkMode()
GPIO.cleanup()
