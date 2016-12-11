#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

if GPIO.input(8):
    return 'Open'
else:
    return 'Closed'
 
time.sleep(1)

GPIO.cleanup()

