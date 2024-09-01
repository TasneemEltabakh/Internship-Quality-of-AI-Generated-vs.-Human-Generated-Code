import numpy as np
import PIL
img_data = PIL.Image.open('w3resource-logo.png' )
img_arr = np.array(img_data) 
print(img_arr)
