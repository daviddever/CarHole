# Example python script for using cover comand to operate Carhole through Home
# Assistant

#!/usr/bin/env python3

import requests
import time
import sys

door_key = 'YOUR KEY'
carhole_url = 'YOUR URL'

def door_status():
    r = requests.post(carhole_url, data={'key':door_key})
    return r.text


def door_open():
    if door_status() == 'Closed':
        r = requests.post(carhole_url, data={'key':door_key})
        time.sleep(10)
        while door_status() == 'Closed':
            time.sleep(10)

        print('Open')
    else:
        print('Already Open')


def door_close():
    if door_status() == 'Open':
        r = requests.post(carhole_url, data={'key':door_key})
        time.sleep(10)
        while door_status() == 'Open':
            time.sleep(10)

        print('Closed')
    else:
        print('Already Closed')


requests.packages.urllib3.disable_warnings()

if len(sys.argv) < 2:
    print('Missing argument. Usage garage.py open|close|status')

elif sys.argv[1].lower() == 'open':
    door_open()

elif sys.argv[1].lower() == 'close':
    door_close()

elif sys.argv[1].lower() == 'status':
    print(str(door_status()))

else:
    print('Invalid arugment. Usage garage.py open|close|status')
