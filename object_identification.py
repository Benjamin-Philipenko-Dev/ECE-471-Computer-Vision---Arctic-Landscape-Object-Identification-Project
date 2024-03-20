import sys
import os
import cv2 # imports OpenCV
import numpy as np
from matplotlib import pyplot as plt #imports matplotlib

# Read the image
img = cv2.imread(("king_penguin.jpg"))
print(img.shape)

cv2.imshow('Penguin Image', img)
cv2.waitKey(0)