#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

from tensorflow.keras.datasets import fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

import matplotlib.pyplot as plt 
from tensorflow.keras.utils import to_categorical

y_cat_test = to_categorical(y_test,10) 
y_cat_train = to_categorical(y_train,10) 
x_train = x_train/255
x_test = x_test/255

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

x_train.shape
x_test.shape

#%%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense, Conv2D, MaxPool2D

model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5)) #Overfitting account 1

model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam', 
              metrics=['accuracy'])

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss',patience=2) #Overfitting account 2
model.fit(x_train, y_cat_train, epochs=10, validation_data=(x_test, y_cat_test),
          callbacks=[early_stop])
model.metrics_names

print(model.summary())

losses = pd.DataFrame(model.history.history) 
losses.head() 
losses[['accuracy','val_accuracy']].plot() 
losses[['loss','val_loss']].plot() 
print(model.metrics_names) 
print(model.evaluate(x_test,y_cat_test,verbose=0))

from sklearn.metrics import classification_report,confusion_matrix
predictions = model.predict(x_test) 
predictions = np.argmax(predictions,axis=1) 
y_cat_test.shape

print(classification_report(y_test,predictions))

clothing_prediction = model.predict(x_test[:10].reshape(10, 28, 28, 1))
clothing_prediction = np.argmax(clothing_prediction, axis=1)
print(clothing_prediction)