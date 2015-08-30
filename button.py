#! /usr/bin/env python

import time
import RPi.GPIO as GPIO
import os

speaker_pin = 4
counter = 0
def start():
        print "Push a button to start!"
        while not GPIO.input(23) :
                x = 0
        print "Start the game!!"
        print "Ready!"
        print "3..."
        sound("on")
        time.sleep(0.65)
        sound("off")
        time.sleep(0.30)
        print "2..."
        sound("on")
        time.sleep(0.65)
        sound("off")
        time.sleep(0.30)
        print "1..."
        sound("on")
        time.sleep(0.65)
        sound("off")
        time.sleep(0.30)
        print "GO!!!"
        
def sound(mode):
        global speaker_pin
        if mode == "on" :
                GPIO.output(speaker_pin,True)
        else :
                GPIO.output(speaker_pin,False)
def blink(counter):
        if(counter >= 2500) :
                GPIO.output(17,True)
                GPIO.output(27,True)
                GPIO.output(22,True)
        elif(counter >= 500) :
                GPIO.output(17,False)
                GPIO.output(27,True)
                GPIO.output(22,True)
        elif(counter >= 50) :
                GPIO.output(17,False)
                GPIO.output(27,False)
                GPIO.output(22,True)
        
        else :
                GPIO.output(17,False)
                GPIO.output(27,False)
                GPIO.output(22,False)
def main():
        
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23,GPIO.IN)
        # LED pin
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(27,GPIO.OUT)
        GPIO.setup(22,GPIO.OUT)
        # Speaker pin
        GPIO.setup(speaker_pin,GPIO.OUT)

        GPIO.output(22,True)
        isPushed = False
        global counter
        global speaker_pin

        start()
        while True:
                if GPIO.input(23) :
                        if not isPushed :
                                isPushed = True
                                counter += 50
                                sound("on")
                                print "push!! +50"
                        else :
                                if counter > 0 : counter -= 10
                                sound("off")
                else :
                        isPushed = False
                        sound("off")
                        if counter > 0 : counter -= 10
                        
                print "current counter :{0}".format(counter)
                blink(counter)
                time.sleep(0.05)

main()
