#!/usr/bin/env python3
import sys, time
import threading
from dmxSender import *

CHANNEL = 1

dmx = dmxSender('ftdi://ftdi:232:B00007AC/1') # see ftdi_urls.py util
dmx.start()

while (True): 
  dmx.setChannel(CHANNEL, 255)
  time.sleep(1)
  dmx.setChannel(CHANNEL, 0)
  time.sleep(2)
