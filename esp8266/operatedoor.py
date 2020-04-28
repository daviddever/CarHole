import machine
import time


def operate(pin):
    operate_pin = machine.Pin(pin, machine.Pin.OUT)
    pin.on()
    time.sleep(1)
    pin.off()
    time.sleep(1)


def check_door(pin):
    check_pin = machine.Pin(0, machine.Pin.IN, None)
    if check_pin:
        return "Open"
    else:
        return "Closed"

    time.sleep(1)
