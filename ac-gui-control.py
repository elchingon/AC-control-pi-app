from guizero import App, Text, Box
from requests import get

def temperature_request(api_url):  
  query_url = api_url
  r = get(query_url)
  if r.status_code != 200:
    print("Error:", r.status_code)
      
  json_resp = r.json()
  id_temp = float(json_resp['temp_1'])
  id2_temp = float(json_resp['temp_2'])
  return id_temp, id2_temp=

def get_temperatures():
  return temperature_request('http://raspberrypi.local:5000');

app = App(title="Temperature Output",layout="grid")

temp1, temp2 = temperature_request('http://raspberrypi.local:5000') 
temp1_box = Box(app,width="100", grid=[0,0])
temp1_label = Text(temp1_box, text=temp1, width="fill")
temp2_label = Text(app, text=temp2, width=70, grid=[1,0])
app.display()

