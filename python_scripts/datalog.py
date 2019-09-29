#!/usr/bin/python

import csv
import altimeter
import accelerometer
from time import sleep
from datetime import datetime

altimeter1 = altimeter.sensor()
accelerometer1 = accelerometer.sensor()

date = str(datetime.now()).replace(" ", "")[:15]
date = date.replace(":", "")

filename = "/home/pi/" + date + ".csv"
file = open(filename, "wb")

fieldnames = ['Altitude', 'Temperature', 'Acceleration', 'Position', 'Time']
writer = csv.DictWriter(file, fieldnames=fieldnames)

writer.writeheader()

sleep(15)

altimeter1.update()
start_altitude = altimeter1.get_altitude()
accelerometer1.update()
start_acceleration = accelerometer1.get_accel_y() 

while True:
	altimeter1.update()
	if int(altimeter1.get_altitude()) > int(start_altitude):
		break
	else:
		sleep(.01)

starttime = float(str(datetime.now().time())[6:])

minutes = 0
t = 0
previous_altitude = 0
minuteincreased = 0
while True:

	altimeter1.update()
	accelerometer1.update()
	
	currenttime = float(str(datetime.now().time())[6:])

	if currenttime < starttime and not minuteincreased:
		minutes += 1
		minuteincreased = True
	elif currenttime > starttime and minuteincreased:
		minuteincreased = False

	time = "%.2f" % float((currenttime  + (minutes * 60)) - starttime)

	# Getting the data from the sensors and formatting it to
	# two decimal places
	writer.writerow({'Altitude': str(altimeter1.get_altitude() - start_altitude),
	                 'Temperature': str(altimeter1.get_temp_fahrenheit()),
	                 'Acceleration': str((accelerometer1.get_accel_y() - start_acceleration) * -1),
	                 'Position': str(accelerometer1.get_mag_y()),
			 'Time': time})



	if previous_altitude == int(altimeter1.get_altitude() - start_altitude):
		t += 1
	elif t > 0:
		t -= 1

	previous_altitude = int(altimeter1.get_altitude() - start_altitude)

	sleep(.01)

	
	
file.close()	






