#!/usr/bin/env python3
import time, threading
from dmxSender import *

dmx = dmxSender()
dmx.start()

for channel in range(1, 5):
  for intensity in range(255, 0, -2):
    dmx.setChannel(channel, intensity)
    time.sleep(0.01)
  dmx.setChannel(channel, 0)

# blink
for _ in range(2):
  dmx.whiteout()
  time.sleep(0.2)

  dmx.blackout()
  time.sleep(0.2)
