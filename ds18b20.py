#!/usr/bin/python
#--------------------------------------
#
#              ds18b20.py
#  Read DS18B20 1-wire temperature sensor
#
# Author : Matt Hawkins
# Date   : 10/02/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

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


if __name__ == '__main__':
  
  while True:
    # Script has been called directly
    id1 = '28-000008ab5f23'
    id1_temp = formatted_temp(id1)
    id2 = '28-000008ab87ce'
    id2_temp = formatted_temp(id2)
    if id1_temp >= 25.5 and id2_temp >= 25.5:
      print("Its' hot")
    elif id1_temp <= 24 and id2_temp <= 24:
      print("Now its cold")

    print "Temp1 : " + '{:.3f}'.format(id1_temp)
    print "Temp2 : " + '{:.3f}'.format(id2_temp)
