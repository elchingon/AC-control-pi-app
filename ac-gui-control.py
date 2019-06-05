#!/usr/bin/env python
from guizero import App, Text, Box

import temperature-control 


def get_temperatures
  temperature-control.temperature_request('http://raspberrypi.local:5000') 

app = App(title="Temperature Output",layout="grid")

temp1, temp2 = temperature-control.temperature_request('http://raspberrypi.local:5000') 
temp1_box = Box(app,width="100", grid=[0,0])
temp1_label = Text(temp1_box, text=temp1, width="fill")
temp2_label = Text(app, text=temp2, width=70, grid=[1,0])
app.display()

