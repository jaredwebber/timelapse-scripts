#!/usr/bin/python3

import datetime
currentDT = datetime.datetime.now()

import os
import time


def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return(temp.replace("temp=",""))

output = open("/media/pi/SSD/Logged Temps/cpu_temp.log", "a")
output.write(currentDT.strftime("%Y\%m\%d %H:%M:%S , ")+measure_temp().replace("'C", ""))
output.close()

