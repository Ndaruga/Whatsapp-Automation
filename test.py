import os
import cv2
import filetype
from PIL import Image


dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "data")
print(os.path.exists(path))

print(path)
# im = Image.open(img)
# im.format

from os import listdir
from PIL import Image
    
for filename in listdir(path):
    if filename.endswith('.png'):
        try:
            img = Image.open('./'+filename) # open the image file
            img.verify() # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename) # print out the names of corrupt files