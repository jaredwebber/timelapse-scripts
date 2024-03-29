#!/usr/bin/python3
import datetime
currentDT = datetime.datetime.now()

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
print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))
  
output = open("/media/pi/SSD/Logged Temps/case_temp.log", "a")
output.write(currentDT.strftime("%Y\%m\%d %H:%M:%S")+ " , "+'{:.3f}'.format(gettemp(id)/float(1000))+"\n")
output.close()
