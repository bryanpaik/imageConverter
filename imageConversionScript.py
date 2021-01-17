## Imports (PIL and numpy are third party packages)
from PIL import Image
import glob
import os
from numpy import asarray
import numpy as np
from numpy.lib import npyio
from sklearn.model_selection import train_test_split

## returns a list of file names in specified folder ('*' means take all files in that directory)
directory ='C:/Users/bryan/Downloads/bryanpaikfireimages'
## Returns a list of file names in specified folder.
images = glob.glob(directory + '/*')

## Length of directory.
dirLength = len(os.listdir(directory))

image_list = [] # creates empty list to store images in

## Loops through all of the images
for image in images:
    ## opens the desired image
    image = Image.open(image)
    ## resizes it into a new image var
    new_image = image.resize((128,128))
    ## appends to image-list var
    image_list.append(new_image)

# Create an empty array of size of directory and of type object (to allow for input of any kind of object)
numpy_array = np.empty(dirLength,dtype=object)
# Create a counter for input into the array
counter = 0
# Loop through all of the images
for image in image_list:
    # Store into numpy_array at index counter
    numpy_array[counter] = image
    # Up the counter by one
    counter+=1

class_array = np.empty(dirLength) ## creates an empty numpy array of the same size

## Splits both arrays into a training set and a testing set (Default parameters for train_test_split is 75% training and 25% testing set)
xTrain, xTest, yTrain, yTest = train_test_split(numpy_array, class_array)	