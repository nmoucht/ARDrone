AR Drone 2.0 Control Software

This repository uses ROS to allow the user to connect to the AR Drone 2.0, command the drone to take off, control the position of the drone, and command the drone to land.

Download github repo: 
https://github.com/AutonomyLab/ardrone_autonomy.git

Other requirements:

ROS

Open CV2

Launch file:
Establishes connection with AR Drone through wifi with standard IP address for AR Drones and gets Navdata.

Command: roslauch launch_drone.launch

Control_drone.py:
Creates publishers for takeoff, landing, and position commands. Commands roll,pitch,yaw, and z by 0.75. Current implementation: launches the drone, asks angle from user, calculates time needed to turn to the angle, turns to the angle, then flies forward or 0.75 seconds. Process is repeated until user commands drone to land

Command to view image feed: rosrun image_view image_view image:=/ardrone/image_raw

image_saver.py: 
Creates publisher and subscriber for AR Drone 2.0 video feed, converts the raw image using Open CV, and saves x amount of images to current directory.
