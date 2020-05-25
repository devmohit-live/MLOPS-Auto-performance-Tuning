# -*- coding: utf-8 -*-
'''
Maintainer:Mohit Singh
Github: @devmohit-live
LinkedIn: devmohitsingh

'''


# importing packages
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

# loading mnist data to their respective variables
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reshaping data for training and testing
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32')

# normalize features for better prediction
X_train = X_train / 255
X_test = X_test / 255

# categorizing labels
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]

# Creating the hyperparameter
with open('data') as f:
  accuracy=f.readline()
  iterator=f.readline() 

# function for creating model
def create_model(i):
  model = Sequential()
  for it in range(i):
    model.add(Conv2D(64, (3, 3), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Flatten())

  for j in range(1,i+1):
    model.add(Dense(256//j, activation='relu'))
    model.add(Dense(256//(j+1), activation='relu'))

  model.add(Dense(num_classes, activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model

# Cheking if we already have optimum accuracy   
if int(accuracy)>95:
  print('Model is already optimized')
else:
  model = create_model(int(iterator))
  model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)
  
  # Finding the accuracy score
  scores = model.evaluate(X_test, y_test, verbose=0)
  acc_score=scores[1]*100
  L = [str(acc_score)+"\n", str(iterator+1)+"\n"]
  with open("data", "w") as fl: 
    # Writing data to a file 
    fl.writelines(L)

