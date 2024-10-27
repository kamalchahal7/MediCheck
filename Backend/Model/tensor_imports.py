import numpy as np
import pandas as pd
import tensorflow as tf
import PIL

from keras.api.layers import Dense,Activation,InputLayer,Flatten,Conv2D,MaxPool2D,BatchNormalization
from keras.api.optimizers import Adam
from keras.api.losses import CategoricalCrossentropy
from keras.api.regularizers import L1,L2
from keras.api.models import Sequential
from keras.api.preprocessing import image_dataset_from_directory, image
from keras.api.saving import load_model

import os, warnings
import random