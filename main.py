
# Step 1: Import Packages/Libraries

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

image_width = 128
image_height = 128
imgage_size = (image_width, image_height)
image_channels = 3

train_directory = './trainImages'
test_directory = './testImages'

def training_data(train_directory):
    files = os.listdir(train_directory)

    category = []
    for file_name in files:
        category = file_name.split('.')[0]
        if category 

