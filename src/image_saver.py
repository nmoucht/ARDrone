import cv2
import cv_bridge
from PIL import Image 
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image as imageX
from cv_bridge import CvBridge, CvBridgeError

def savePic(self):
    for x in range(3):	
           self.image_pub = rospy.Publisher("ardrone/image",imageX)   
	   msg=rospy.wait_for_message('ardrone/image', imageX)
	   self.bridge = CvBridge()  
	   img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
	   cv2.imwrite("Droneim"+x+".jpg", img)
self.savePic()
