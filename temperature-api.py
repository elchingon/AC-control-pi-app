#!/usr/bin/python
#--------------------------------------
#
#              ds18b20.py
#  Read DS18B20 1-wire temperature sensor
#--------------------------------------

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return combined_temps()

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()

    return int(mytemp[1])

  except:
    return 99999

def formatted_temp(id):
  return gettemp(id)/float(1000)

def combined_temps():
  id1 = '28-000008ab5f23'
  id1_temp = formatted_temp(id1)
  id2 = '28-000008ab87ce'
  id2_temp = formatted_temp(id2)
  return jsonify(temp_1='{:.3f}'.format(id1_temp),
                 temp_2='{:.3f}'.format(id2_temp))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
  
