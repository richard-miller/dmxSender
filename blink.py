#!/usr/bin/env python3
import sys, time, threading
from dmxSender import *

CHANNEL = 1

dmx = dmxSender()
dmx.start()

while True: 
  dmx.setChannel(CHANNEL, 255)
  sys.stdout.write("\rBLINK - (Type ^C to abort)")
  time.sleep(1)
  dmx.setChannel(CHANNEL, 0)
  sys.stdout.write("\rblink - (Type ^C to abort)")
  time.sleep(2)
