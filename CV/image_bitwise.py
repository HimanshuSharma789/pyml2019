#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv1.png')


# In[3]:


# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]


# In[9]:


# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow("r", img2gray)
# cv2.imshow("rr", mask)
# cv2.imshow("rrr", mask_inv)


# In[17]:


# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# cv2.imshow('img1_bg',img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# cv2.imshow('img2_fg',img2_fg)


# In[18]:


# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
# cv2.imshow('dst', dst)


# In[19]:


cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



