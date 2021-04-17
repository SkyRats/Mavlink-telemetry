#!/usr/bin/env python3

from pymavlink import mavutil
import time



if __name__ == "__main__":
	#Telemetria:
	mav = mavutil.mavlink_connection("/dev/ttyUSB0", autoreconnect=True, baud=57600)

	#USB:
	#mav = mavutil.mavlink_connection("/dev/ttyACM0", autoreconnect=True, baud=57600)

	#Gazebo:
	#mav = mavutil.mavlink_connection('udpin:localhost:1450')
	print("Conectou")
	for i in range(10):
		print("Testando:")
		print(mav.wait_heartbeat())
		time.sleep(1)
	distance = 10
	while(True):
		if distance == 10:
			distance = 1000
		elif distance == 1000:
			distance = 10
		#'time_boot_ms', 'min_distance', 'max_distance', 'current_distance', 'type', 'id', 'orientation', and 'covariance'
		mav.mav.distance_sensor_send(10, 20, 1200, distance, 0, 0, 25, 255)
		print("SENT")
		#print(dir(mav.mav.distance_sensor_send()))
			



