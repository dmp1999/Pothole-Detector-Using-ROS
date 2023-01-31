#!usr/bin/env python

import rospy 
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def getKey(key_timeout):
	settings = termios.tcgetattr(sys.stdin)
	tty.setraw(sys.stdin.fileno())
	rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
	if rlist:
		key = sys.stdin.read(1)
	else:
		key = ''
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	#print("a")
	return key

v=Twist()
rospy.init_node('Commander_node')
pub = rospy.Publisher('cmd_vel',Twist,queue_size = 100)
rate = rospy.Rate(5)
command = "c"
v.linear.x = 0
v.angular.z = 0
pub.publish(v)

while not rospy.is_shutdown():
	
	if command == "a":
		v.linear.x = v.linear.x + 0.5
		pub.publish(v)
		#print("Moving Left")
		command = "c"

	elif command == "s":
		v.angular.z = v.angular.z - 0.5
		pub.publish(v)
		#print("Moving Backwards")
		command = "c"

	elif command == "w":
		v.angular.z = v.angular.z + 0.5
		pub.publish(v)
		#print("Moving Forward")
		command = "c"

	elif command == "d":
		v.linear.x = v.linear.x - 0.5
		pub.publish(v)		
		#print("Moving Right")
		command = "c"

	elif command == "q":
		v.linear.x = 0
		v.angular.z = 0
		pub.publish(v)
		#print("stop")
		command = "c"

	else:
		command = getKey(100)	#press t to terminate control mode
		if command == "t":
			break
	rate.sleep()






