# CarHole

~~Set of scripts~~ Microservice for controlling my garage door through a raspberry pi

![alt text](https://frinkiac.com/meme/S06E23/1075707.jpg?b64lines=IEhFWSwgRkVMTEFTLCBUSEUgR0FSQUdFLgogT09ILCBMQS1ESS1EQSwgTVIuIEZSRU5DSAogTUFOLiAKCgoKCgpXSEFUIERPIFlPVSBDQUxMIElUPwoKCiBBIENBUiBIT0xFLg== "A counterfit jeans ring operating out of my carhole!")

Wiring instructions from [Idiot’s Guide to a Raspberry Pi Garage Door Opener by Chris Driscoll](https://web.archive.org/web/20161108145900/http://www.driscocity.com/idiots-guide-to-a-raspberry-pi-garage-door-opener/) 

Site is currently flagged for malware, link goes to [Internet Archive](https://archive.org/web/) cache.

##Installation

1. Wire up the Raspberry Pi with the guide above
2. sudo apt-get install python-pip
3. sudo pip install flask
4. Copy SSL cert and key to directory or generate a self-signed one: openssl req -x509 -newkey rsa:4096 -keyout carholekey.pem -out carholecert.pem -days 3650 -nodes
5. sudo python carhole.py

The server runs on https on port 443

A GET request to /operate will open the door.
A GET request to /check_door will return Open or Closed


**This is not secure at all!**

###checkdoor.py
Short script to check state of door, returns Open or Closed

