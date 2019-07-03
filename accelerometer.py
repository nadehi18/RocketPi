# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the LSM303 module.
import Adafruit_LSM303

class sensor():
	def __init__(self):

		# Create a LSM303 instance.
		self.lsm303 = Adafruit_LSM303.LSM303()
		
		self.accel_x = None
		self.accel_y = None
		self.accel_z = None

		self.mag_x = None
		self.mag_y = None
		self.magz = None

	def update(self):

	    # Read the X, Y, Z axis acceleration values and print them.
	    accel, mag = self.lsm303.read()
	    # Grab the X, Y, Z components from the reading and print them out.
	    self.accel_x, self.accel_y, self.accel_z = accel
	    self.mag_x, self.mag_z, self.mag_y = mag

	def get_accel_x(self):
		return(self.accel_x)

	def get_accel_y(self):
		return(self.accel_y)

	def get_accel_z(self):
		return(self.accel_z)

	
	def get_mag_x(self):
		return(self.mag_x)
	
	def get_mag_y(self):
		return(self.mag_y)

	def get_mag_z(self):
		return(self.mag_z)
	
