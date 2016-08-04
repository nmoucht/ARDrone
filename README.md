This repo allows the user to connect to the AR Drone 2.0, command the drone to take off, control the position of the drone, and command the drone to land.

Download github repo: 
https://github.com/AutonomyLab/ardrone_autonomy.git

Launch file:
Establishes connection with AR Drone through wifi with standard IP address for AR Drones.

Command: roslauch launch_drone.launch

Control_drone.py:
Creates publishers for takeoff, landing, and position commands. Commands pitch by 1 radian. Sends drone forward for 2 seconds, pauses, then sends the drone backward for 2 seconds.
