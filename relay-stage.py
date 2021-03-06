#!/usr/bin/env python
import requests
import json
import time
import relay

api_key=""
id1_max=25
id2_max=25
id3_max=25
id1_min=24
id2_min=24
id3_min=24


def temperature_request(api_url):  
  query_url = api_url
  r = requests.get(query_url)
  if r.status_code != 200:
    print "Error:", r.status_code
      
  json_resp = r.json()
  id_temp = float(json_resp['temp_1'])
  id2_temp = float(json_resp['temp_2'])
  return id_temp, id2_temp

def run_ac_control():
  while True:  
    try:
      id1_temp, id2_temp  = temperature_request('http://raspberrypi.local:5000')
      id3_temp = id1_temp
      relay.trigger_relay(False, 17)
      relay.trigger_relay(False, 27)
      relay.trigger_relay(False, 22)
      
      if id1_temp >= id1_max and id2_temp >= id2_max and id3_temp >= id3_max:
        print("Compressor on")
        relay.trigger_relay(False, 23)
        relay.trigger_relay(False, 24)
        relay.trigger_relay(False, 25)
      elif id1_temp <= id1_min and id2_temp <= id2_min and id3_temp <= id3_min:
        print("Compressor off")
        relay.trigger_relay(True, 23)
        relay.trigger_relay(True, 24)
        relay.trigger_relay(True, 25)
      
      print("Temp1:"+str(id1_temp))
      print("Temp2:"+str(id2_temp))
      print("Temp3:"+str(id3_temp))
      
      time.sleep(5)
    except requests.exceptions.RequestException as err:
      print ("OOps: Something Else",err)
      time.sleep(5)
      continue
    except requests.exceptions.HTTPError as errh:
      print ("Http Error:",errh)
      time.sleep(5)
      continue
    except requests.exceptions.ConnectionError as errc:
      print ("Error Connecting:",errc)
      time.sleep(5)
      continue
    except requests.exceptions.Timeout as errt:
      print ("Timeout Error:",errt)     
      time.sleep(5)
      continue
    except KeyboardInterrupt:
      print "Quit"
    #relay.trigger_relay(True)

if __name__ == '__main__':
  run_ac_control()
  
