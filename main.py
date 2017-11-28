from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import binarycreator
#test with very small data set


#LOAD TRAINING DATA
trainingdataset = pd.read_csv("trainingdata.txt")
#9 input variable
x = trainingdataset.iloc[:, 0:9].values

#1 output variable
y = trainingdataset.iloc[:, 9].values  #TODO play around with?

#LOAD TEST DATA
testdataset = pd.read_csv('testdata.txt')
#print(testdataset)          #TODO: remove after testing
#print(trainingdataset)

# CREATE MODEL
model = Sequential()

# DEFINE MODEL
# create hidden layer  #TODO: will want to play around with units
model.add(Dense(units=9, input_dim=9,activation='relu'))  #4 inputs,
model.add(Dense(units=1, activation='sigmoid'))
# Adam is a gradient descent optimization algorithm used for tuning data
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

#FIT MODEL
#batch size = # of instances evaluated before weights are assigned
model.fit(x, y, epochs=150, batch_size=10)

#EVALUATE MODEL
scores = model.evaluate(x,y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

