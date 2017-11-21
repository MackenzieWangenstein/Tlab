from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import binarycreator
#test with very small data set

trainingdataset = pd.read_csv("trainingdata.txt")
testdataset = pd.read_csv('testdata.txt')
# print(testdataset)
# print(trainingdataset)
#
binarycreator.createAndClassify()
# #create model
# model = Sequential()
#
# #create hidden layer
# #will want to play around with units
# model.add(Dense(units=4, input_dim=4,activation='relu'))  #4 inputs,
# model.add(Dense(units=1, activation='sigmoid'))
# #adam is a gradient descent optimization algorithm used for tuning data
# model.compile(loss='mean_squared_error',)