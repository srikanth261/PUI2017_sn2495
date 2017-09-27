# Author: Srikanth
##############################
# Assignement 2 for HW2 of PUI2017
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
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python  aSimplePythonScript.py YourNameHerepython get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()


mtaapikey = sys.argv[1]
bus_line = sys.argv[2]
file_name = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" \
+ mtaapikey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicles = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

next_stops = []

for i in vehicles:
    
    location = i['MonitoredVehicleJourney']['VehicleLocation']
    latitude = location['Latitude']
    longitude = location['Longitude']
    
    try:
        next_stop_name = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]\
        ['Extensions']['Distances']['PresentableDistance']
        
    except TypeError or KeyError:
        next_stop_name = "N/A"
        status = "N/A"
    
    next_stops.append([latitude,longitude,next_stop_name,status])

busline = pd.DataFrame(next_stops)

busline.columns= ['latitude','longitude','stop name','stop status']

busline.to_csv(str(file_name))


