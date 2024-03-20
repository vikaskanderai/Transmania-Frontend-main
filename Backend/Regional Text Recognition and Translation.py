#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install imutils')


# In[17]:


pip install opencv-python


# In[18]:


from imutils import paths
import cv2


# ### Capturing the image

# In[19]:


from datetime import datetime


# In[20]:


cam = cv2.VideoCapture(0)
cv2.namedWindow("Webcam for Transmania")

img_counter=0
while True:
    ret,frame= cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test",frame)
    
    k=cv2.waitKey(1)
    if k%256==27:
        print("escape successful")
        break
    elif k%256==32:
            img_name="opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            print("frame captured")
            img_counter+=1
            break
    
cam.release()
cv2.destroyAllWindows()


# In[21]:


image=cv2.imread('opencv_frame_0.png') 
cv2.imshow("frame received",image)
cv2.waitKey(0)


# In[22]:


get_ipython().system('pip install pytesseract')
get_ipython().system('pip install matplotlib')

import cv2
import os
import pytesseract
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

image_path = "opencv_frame_0.png"
image = cv2.imread(image_path)


# In[23]:


#sharpening the image

#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 
  
# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
  
# Sharpen the image 
sharpened_image = cv2.filter2D(image, -1, kernel) 
  
#Save the image 
cv2.imwrite('sharpened_image.jpg', sharpened_image) 
  
#Plot the sharpened image 
plt.subplot(1, 2, 2) 
plt.title("Sharpening") 
plt.imshow(sharpened_image) 
plt.show()
image_path = "sharpened_image.jpg"
image = cv2.imread(image_path)


# In[24]:


#sharpening the image

#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 
  
# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
  
# Sharpen the image 
sharpened_image = cv2.filter2D(image, -1, kernel) 
  
#Save the image 
cv2.imwrite('sharpened_image.jpg', sharpened_image) 
  
#Plot the sharpened image 
plt.subplot(1, 2, 2) 
plt.title("Sharpening") 
plt.imshow(sharpened_image) 
plt.show()
image_path = "sharpened_image.jpg"
image = cv2.imread(image_path)


# In[25]:


#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 

# Inverse by subtracting from 255 
inverse_image = 255 - image 

#Save the image 
cv2.imwrite('inverse_image.jpg', inverse_image) 
#Plot the Inverse image 
plt.subplot(1, 2, 2) 
plt.title("Inverse color") 
plt.imshow(inverse_image) 
plt.show()
image_path = "inverse_image.jpg"
image = cv2.imread(image_path)


# In[ ]:




