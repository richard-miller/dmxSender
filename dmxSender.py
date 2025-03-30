# requirements
#
# python=3
# pyftdi

import time, threading
import pyftdi.serialext

class dmxSender:

  # find avail serialPort via ftdi_urls.py (incl in pyftdi package)
  
  def __init__(self, serialPort = 'ftdi://ftdi:232:B00007AC/1'):
    try:
      self.serial = pyftdi.serialext.serial_for_url(serialPort, baudrate=250000, stopbits=2)
    except:
      print("Error: could not open Serial Port")
      sys.exit(0)

    self.dmxData = [bytes([0])] * 513
        
  def setChannel(self, chan, intensity):
    self.dmxData[chan] = bytes([intensity])
        
  def blackout(self):
    for i in range(1, 512, 1):
      self.dmxData[i] = bytes([0])

  def whiteout(self):
    for i in range(1, 512, 1):
      self.dmxData[i] = bytes([255])
        
  def render(self):
    sdata = b''.join(self.dmxData)
    self.serial.send_break(duration=0.001)
    self.serial.write(sdata)

  def render_thread(self):
    while True:
      self.render()
      time.sleep(0.005)
  
  def start(self):
    self.dmx_thread = threading.Thread(target=self.render_thread)
    self.dmx_thread.daemon = True
    self.dmx_thread.start()
