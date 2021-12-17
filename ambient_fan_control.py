#!/usr/bin/python3

import RPi.GPIO as GPIO
import os
import datetime

currentDT = datetime.datetime.now()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

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
 
if __name__ == '__main__':
 
  # Script has been called directly
  id = '28-0308979425ec'
#print ("Temp : " + '{:.3f}'.format(gettemp(id)/float(1000)))


def measure_temp():
        #temp = os.popen("vcgencmd measure_temp").readline()
        #tempmod=(temp.replace("temp=",""))
        #return(float)(tempmod.replace("'C",""))
        return gettemp(id)/float(1000)
    
finaltemp = measure_temp()

print(finaltemp)

if finaltemp >= 28:
    GPIO.output(18, GPIO.HIGH)
else:
    GPIO.output(18, GPIO.LOW)
        
