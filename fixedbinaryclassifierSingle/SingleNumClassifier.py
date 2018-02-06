from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
#test with very small data set


#LOAD TRAINING DATA
trainingdataset = pd.read_csv("trainingdata.txt")
#9 input variable
x_train = trainingdataset.iloc[:, 0:9].values

#1 output variable
y_train = trainingdataset.iloc[:, 9].values  #TODO play around with?

#print(testdataset)          #TODO: remove after testing
#print(trainingdataset)

# CREATE MODEL
model = Sequential()

# DEFINE MODEL
# create hidden layer  #TODO: will want to play around with units
model.add(Dense(units=9, input_dim=9,activation='relu'))  #9 inputs,
model.add(Dense(25, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
# Adam is a gradient descent optimization algorithm used for tuning data
#binary_crossentropy
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

#added comment to remove -- TODO: remove
#changed batch_size
#FIT MODEL
#batch size = # of instances evaluated before weights are assigned
print("fitting model to training data.")
model.fit(x_train, y_train, epochs=1000,verbose=0, batch_size=x_train.shape[0])


print("evaulating model on training data")
#EVALUATE MODEL
scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# #test prediction on training data
print("Running prediction on training data to determine model performance")
predictions = model.predict(x_train)
rounded = [round(x[0]) for x in predictions]
print("rounded results for predicted outputs of training data. ")
print(rounded)

#round results - can combine this step and the next into one
for i in range(0, len(rounded)):
    if rounded[i] != y_train[i]:
        print("something went wrong. outcome not predicted correctly! ")
        print("training data values: ", x_train[i])
        print("training data expected outcome: ", y_train[i])
        print("actual prediction value: ", rounded[i])

print("Testing data predictions on test data set")

#LOAD TEST DATA
test_data_set = pd.read_csv('testdata.txt')

x_test = test_data_set.iloc[:,0:9].values
y_test = test_data_set.iloc[:, 9].values

test_predictions = model.predict(x_test)
rounded_test = [round(x[0]) for x in test_predictions]
print("test data set predicted values(rounded):")
print(rounded_test)

print("Comparing predicted results against actual results.")
for i in range(0, len(rounded_test)):
    if rounded_test[i] != y_test[i]:
        print("something went wrong. outcome not predicted correctly! ")
        print("test data values: ", x_test[i])
        print("test data expected outcome: ", y_test[i])
        print("actual prediction value: ", rounded_test[i])
