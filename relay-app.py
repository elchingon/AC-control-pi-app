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
      query_url = api_url
      r = requests.get(query_url)
      if r.status_code != 200:
        print "Error:", r.status_code
      
      
      json_resp = r.json()
      
      id1_temp = float(json_resp['temp_1'])
      id2_temp = float(json_resp['temp_2'])
      
      if id1_temp >= id1_max and id2_temp >= id2_max:
        print("Compressor on")
        relay.trigger_relay(False)
      elif id1_temp <= id1_min and id2_temp <= id2_min:
        print("Compressor off")
        relay.trigger_relay(True)
      
      print("Temp1:"+str(id1_temp))
      print("Temp2:"+str(id2_temp))
      
      time.sleep(5)
      #relay.trigger_relay(True)
  except KeyboardInterrupt:
    print "Quit"

