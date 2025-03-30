#!/usr/bin/env python3
import time, threading
from dmxSender import *

CHANNEL = 1

dmx = dmxSender()
dmx.start()

while True: 
  dmx.setChannel(CHANNEL, 255)
  time.sleep(1)
  dmx.setChannel(CHANNEL, 0)
  time.sleep(2)
