'''
This program gets the raw image from the AR Drone 2.0, and in a loop, publishes 
the image, waits for the message, converts the raw image using Open CV, and saves 
the image as droneIm(x).jpg. Though this code is in a seperate class, it can easily 
be implemented in other python scripts.
'''
import cv2s
from PIL import Image
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image as imageX
from cv_bridge import CvBridge, CvBridgeError
class image_save():
     def __init__(self):
	    self.bridge = CvBridge()  
	    for x in range(0,3):
            	self.image_pub = rospy.Publisher("/ardrone/image_raw",imageX) 
   	    	msg=rospy.wait_for_message("/ardrone/image_raw", imageX)
   	    	img = self.bridge.imgmsg_to_cv2(msg, "bgr8")    
   	    	cv2.imwrite("droneIm"+str(x)+".jpg", img)

def main():
      rospy.init_node('save_picture', anonymous = True)
      image_save()
      
if __name__ == '__main__': 
 	try: 
		main()
	except rospy.ROSInterruptException: 
       			pass
