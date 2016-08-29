#!/usr/bin/env python
'''
Simple program to controll AR Drone 2.0
Needed:
ROS
https://github.com/AutonomyLab/ardrone_autonomy.git
ROS command for video feed:
rosrun image_view image_view image:=/ardrone/image_raw
'''
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time as timer

rospy.init_node('takeoff', anonymous=True)
pubT = rospy.Publisher("ardrone/takeoff", Empty, queue_size=1)
commandDrone= rospy.Publisher('/cmd_vel', Twist, queue_size=1)
pubL = rospy.Publisher("ardrone/land", Empty, queue_size=1)
rate = rospy.Rate(10) # 10hz

def control():
	takeoff()
	rospy.sleep(5)
	z=True
	time=0
	while(z==True):
		angle=raw_input("Enter an angle between 90 and -90, or 'land': ")
		
		if(angle=="land"):
			z=False
		else:
			print "Calculating time..."
			a=float(angle)
			if(a>0):
				time=((4.3739*(10**-5))*(a**2))+((7.8375*(10**-3))*a)
				print "Executing parameter..."
				SendCommandClock()
				timer.sleep(time)
			elif(a<0):
				a*=-1
				time=((5.0178*(10**-5))*(a**2))+((0.0101)*a)
				print "Executing parameter..."
				SendCommandCounter()
				timer.sleep(time)
			SendCommandF()
			timer.sleep(0.75)
			ResetCommand()
			time=0
	rospy.sleep(2)
	land()
	print "done."
#39-23
def takeoff():
	print "Taking off..."
	for x in range(0,5):
		pubT.publish(Empty())
		rate.sleep()
def land():
	print "Landing..."
	for x in range(0,5):
		pubL.publish(Empty())
		rate.sleep()

def SendCommandF(roll=0,pitch=0.75,yaw_velocity=0,z_velocity=0):
	commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)
	#rospy.sleep(10)
	#command.linear.x=-50
	#commandDrone.publish(command)
#pitch +forward -backward
#yaw +counterclockwise -clockwise

def SendCommandClock(roll=0,pitch=0,yaw_velocity=-0.75,z_velocity=0):
	#commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)

def SendCommandCounter(roll=0,pitch=0,yaw_velocity=0.75,z_velocity=0):
	#commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)

def ResetCommand(roll=0,pitch=0,yaw_velocity=0,z_velocity=0):
	#commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)

if __name__ == '__main__':
	try:
		control()
	except rospy.ROSInterruptException:
		pass
