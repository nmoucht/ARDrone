import cv2
import numpy as np
from PIL import Image
from resizeimage import resizeimage

img = cv2.imread('office3.jpg',0)
#img=cv2.resize(zx, (960,540))
#img=resizeimage.resize_cover(zx,[200,100])
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

cond=True
param=10

while (cond):
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,40,
                            param1=100,param2=param,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    if(circles[0].size/3>0 and circles[0].size/3<3):
        cond=False
    elif(circles[0].size/3==0):
        parm-=10
    else:
        param+=10
print param


for i in circles[0,:]:
    # draw the outer circle
    print (i[0],i[1])
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

print (circles[0].size)/3

if ((circles[0].size)/3==2):
    cv2.circle(cimg,((circles[0][0][0]+circles[0][1][0])/2,(circles[0][0][1]+circles[0][1][1])/2),20,(0,255,255),2)
# draw the center of the circle
    cv2.circle(cimg,((circles[0][0][0]+circles[0][1][0])/2,(circles[0][0][1]+circles[0][1][1])/2),2,(0,255,255),3)

elif((circles[0].size)/3==3):
    cv2.circle(cimg,((circles[0][0][0]+circles[0][1][0]+circles[0][2][0])/3,(circles[0][0][1]+circles[0][1][1]+circles[0][2][1])/3),20,(0,255,255),2)
# draw the center of the circle
    cv2.circle(cimg,((circles[0][0][0]+circles[0][1][0]+circles[0][2][0])/3,(circles[0][0][1]+circles[0][1][1]+circles[0][2][1])/3),2,(0,255,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
