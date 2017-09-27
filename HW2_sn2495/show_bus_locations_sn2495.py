# Author: Srikanth
##############################
# Assignement 1 for HW2 of PUI2017
# 
##############################

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function
# the next import allows me to read line input arguments
import sys
#import pylab as pl
import os
import json
import pandas as pd

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


# this line checks how many arguments are passed to python
# the arguments are stored in sys.argv which is a list
# the first argument is the name of the code
# so sys.argv is a list with at least one element
# with your name in input it will be a list of 2
# if you add more than one word as argument it will give you an error as well
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  aSimplePythonScript.py YourNameHere")
    sys.exit()


mtaapikey = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" \
+ mtaapikey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicles = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

bus_num = 0

print( "Bus Line : ", bus_line)

print( "Number of Active Buses: ",len(vehicles))


for i in vehicles:
         
    location = i['MonitoredVehicleJourney']['VehicleLocation']
    latitude = location['Latitude']
    longitude = location['Longitude']
    
    print("Bus" + str(bus_num) + " is at latitude " + str(latitude) + " and longitude " + str(longitude))
    
    bus_num += 1



