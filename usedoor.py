import RPi.GPIO as GPIO
import time
 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
 
# Operate door
GPIO.output(40, True)
time.sleep(1)
GPIO.output(40, False)
time.sleep(1)
 
# Clear state
GPIO.cleanup()

