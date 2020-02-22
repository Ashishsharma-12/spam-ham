# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:08:12 2020

@author: NILESH
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras import *
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

X = pickle.load(open("x.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))

x_train = tf.keras.utils.normalize(X,axis = 1)

model = Sequential()

model.add(Conv2D(64,(3,3),input_shape = X.shape[1:],activation = tf.nn.relu))
#model.add(Activation="relu")
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(64,(3,3),input_shape = X.shape[1:],activation = tf.nn.relu))
#model.add(Activation="relu")
model.add(MaxPooling2D(pool_size = (2,2)))


model.add(Flatten())
model.add(Dense(32))

model.add(Dense(1,activation = tf.nn.sigmoid))
#model.add(Activation("sigmoid"))

model.compile(optimizer = 'adam',
             loss = 'binary_crossentropy',
             metrics = ['accuracy'])

model.fit(X,y,batch_size=12, validation_split=0.01,epochs = 3)

model.save('E:/spam_ham.yml')
