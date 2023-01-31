#!usr/bin/env python

import rospy 
from geometry_msgs.msg import Twist
import numpy as np
from tensorflow import keras
from keras.models import Model
import cv2
import math 
import os

IMG_SIZE=256
rate = rospy.Rate(5)

model=keras.models.load_model('model_1.h5')

while not rospy.is_shutdown():
	
	os.system('rosrun image_view image_saver image:=/bot_urdf1/camera1/image_raw')

        img1 = cv2.imread('frame0000.jpg', cv2.IMREAD_COLOR)
        img = cv2.resize(img1, (IMG_SIZE,IMG_SIZE))
	
	X=np.array(img)
	prediction=model.predict(X)
	#print(prediction)
	
	y_pred = np.argmax(prediction)
	#print(y_pred)
	
	if(y_pred = True):
		print('Pothole Detected')
	else:
		print('Plain Road')

	rate.sleep()






