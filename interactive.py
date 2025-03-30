#!/usr/bin/env python3
import sys, time
from dmxSender import *

CHANNEL = 1

dmx = dmxSender()
dmx.start()

while (True): 
  channel = int(input("Channel: "))
  intensity = int(input("Intensity: "))
  dmx.setChannel(channel, intensity)
  print("")
