#!/usr/bin/env python
import requests
import json
import time
import relay

api_url="http://raspberrypi.local:5000"
api_key=""
id1_max=26
id2_max=26
id1_min=24
id2_min=24

if __name__ == '__main__':
  try:
    while True:  
      relay.trigger_relay(True, 17)
      print "Turning off 17"
      relay.trigger_relay(True, 27)
      print "Turning off 27"
      relay.trigger_relay(True, 22)
      print "Turning off 22"
      relay.trigger_relay(True, 23)
      print "Turning off 23"
      relay.trigger_relay(True, 24)
      print "Turning off 24"
      relay.trigger_relay(True, 25)
      print "Turning off 25"
      time.sleep(5)
      #relay.trigger_relay(True)
  except KeyboardInterrupt:
    print "Quit"

