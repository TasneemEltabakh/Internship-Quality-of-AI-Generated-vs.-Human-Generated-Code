# import required libraries
from PIL import Image
import numpy as gfg


# read an image
img = Image.open('geeksforgeeks.jpg')


# convert image object into array
imageToMatrice = gfg.asarray(img)


# printing shape of image
print(imageToMatrice.shape)