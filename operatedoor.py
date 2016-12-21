import RPi.GPIO as GPIO
import time

def operate(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

    # Operate door
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)

    # Clear state
    GPIO.cleanup()

def check_door(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
     
    if GPIO.input(pin):
        return 'Open'
    else:
        return 'Closed'
  
    time.sleep(1)
    GPIO.cleanup()

