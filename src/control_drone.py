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

def takeoff(): 
   pubT = rospy.Publisher("ardrone/takeoff", Empty, queue_size=10 ) 
   rospy.init_node('takeoff', anonymous=True) 
   rate = rospy.Rate(10) # 10hz 
   for x in range(0,5): 
       pubT.publish(Empty()) 
       rate.sleep()
   rospy.sleep(5)
   commandTimer = rospy.Timer(rospy.Duration(100/1000.0),SendCommandF)
   rospy.sleep(2)
   commandTimer = rospy.Timer(rospy.Duration(100/1000.0),ResetCommand)
   rospy.sleep(2)
   commandTimer = rospy.Timer(rospy.Duration(100/1000.0),SendCommandB)
   rospy.sleep(2)
   commandTimer = rospy.Timer(rospy.Duration(100/1000.0),ResetCommand)
   rospy.sleep(2)
   land()

def SendCommandF(self,roll=0,pitch=1,yaw_velocity=0,z_velocity=0):
	commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)
	print command
	#rospy.sleep(10)
	#command.linear.x=-50
	#commandDrone.publish(command)
	
#pitch +forward -backward
#yaw +counterclockwise -clockwise
def SendCommandB(self,roll=0,pitch=-1,yaw_velocity=0,z_velocity=0):
	commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)
	print command

def ResetCommand(self,roll=0,pitch=0,yaw_velocity=0,z_velocity=0):
	commandDrone= rospy.Publisher('/cmd_vel', Twist)
	command=Twist()
	command.linear.x = pitch
	command.linear.y = roll
	command.linear.z = z_velocity
	command.angular.z = yaw_velocity
	commandDrone.publish(command)

def land():
	rate = rospy.Rate(10)
	pubL = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
	for x in range(0,5): 
       		pubL.publish(Empty()) 
       		rate.sleep()
if __name__ == '__main__': 
   try: 
       takeoff() 
   except rospy.ROSInterruptException: 
       pass
