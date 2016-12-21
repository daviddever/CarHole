# CarHole

~~Set of scripts~~ Microservice for controlling my garage door from a Raspberry Pi

![alt text](https://frinkiac.com/meme/S06E23/1075707.jpg?b64lines=IEhFWSwgRkVMTEFTLCBUSEUgR0FSQUdFLgogT09ILCBMQS1ESS1EQSwgTVIuIEZSRU5DSAogTUFOLiAKCgoKCgpXSEFUIERPIFlPVSBDQUxMIElUPwoKCiBBIENBUiBIT0xFLg== "A counterfit jeans ring operating out of my carhole!")

Wiring instructions from [Idiot’s Guide to a Raspberry Pi Garage Door Opener by Chris Driscoll](https://web.archive.org/web/20161108145900/http://www.driscocity.com/idiots-guide-to-a-raspberry-pi-garage-door-opener/) 

Site is currently flagged for malware, link goes to [Internet Archive](https://archive.org/web/) cache.

##Installation

1. Wire up the Raspberry Pi with the guide above
2. sudo apt-get install python-pip
3. sudo pip install flask
4. Copy SSL cert and key to directory or generate a self-signed one: `openssl req -x509 -newkey rsa:4096 -keyout carholekey.pem -out carholecert.pem -days 3650 -nodes`
5. Edit `config-example` and save as `config.py`
6. sudo python carhole.py

The server runs https on port 443

There is a secret key configured in `config.py` that must be included in `application/x-www-form-urlencoded` content type in each request or the request will return a `Invalid Key` error.

A `POST` request to `/operate` will operate the door.

A `POST` request to `/checkdoor` will return `Open` or `Closed`

**Security Warning!**

While this script makes efforts to operate securely, nothing is perfect and new vulnerabilites are discovered all the time, be sure to evaluate and mitigate the potential risks by blocking all, or limiting to only port 443, exposure to the Internet and apply updates to keep all components as new fixes are released.


Example of a Python script to check door status

```python
import requests

r = requests.post('https://YOUR ADDRESS/checkdoor', data={'key':'YOUR KEY'}, verify='YOUR CERTFILE')

print r.text
```
##Stand Alone Scripts
These scripts can be run from the shell independently of carhole.py

###checkdoor.py
Checks state of door, returns `Open` or `Closed`

###useedoor.py
Operates the door

###tasker.xml
Task to import into Tasker to operate the door
