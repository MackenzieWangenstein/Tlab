import numpy as np
import perceptronutility as putil
import matplotlib.pyplot as plt
import sys


class NeuralNet(object):
	# todo: refactor to get rid of param for data_set counts -- just use shape instead
	#TODO: consider creating config object - use builder pattern to avoid using so many parameters
	def __init__(self,
	             hidden_node_count,
	             learning_rate,
	             momentum,
	             output_node_count,
	             training_data,
	             training_labels_matrix,
	             validation_data,
	             validation_labels_matrix,
	             epochs,
	             print_details):

		"""

		:param hidden_node_count:
		:param learning_rate:
		:param momentum:
		:param output_node_count:
		:param training_data: the inputs associated with each training example,**training data has bias already appended
		:param training_count:
		:param training_labels_matrix: the expected class value in vector form for each training example
		:param validation_data:   the inputs associated with each test example
		:param validation_labels_matrix: the expected class value in vector form for each test example
		:param epochs:

		Notes:
					Confusion_matrix: The confusion_matrix[i][j] gives us the number of data_examples that were placed
					into that classification case. i is the actual predicted class for the training element, where j is
					the target class value. Diagonal values represents true positive predictions, while all other values
					are considered false positive predictions.

					accuracy = sum of all correct predictions(confusion_matrix diagonal values) / sum of all predictions
		"""
		#TODO: update comments
		self.input_node_count = training_data.shape[1]  # should be 785
		self.hidden_node_count = hidden_node_count  # 20
		self.output_node_count = output_node_count  # 10

		self.learning_rate = learning_rate
		self.momentum = momentum

		self.hidden_layer_weights = np.random.uniform(low=-0.05, high=0.05,
		                                              size=(training_data.shape[1],  hidden_node_count))  # input nodes to hidden layer nodes
		print("shape of hidden layer weights: ", self.hidden_layer_weights.shape)
		self.output_layer_weights = np.random.uniform(low=-0.05, high=0.05,
		                                              size=(hidden_node_count + 1, output_node_count))#shape HNC+1xONC
		self.training_data = training_data
		self.training_data_size = training_data.shape[0]
		self.training_labels = training_labels_matrix
		self.validation_data = validation_data
		self.validation_data_size = validation_data.shape[0]
		self.validation_labels = validation_labels_matrix

		self.bias = 1
		self.epochs = epochs
		self.training_confusion_matrix = np.zeros((self.output_node_count, self.output_node_count))
		self.validation_confusion_matrix = np.zeros((self.output_node_count, self.output_node_count))

		self.training_error_history = np.zeros(epochs)
		self.training_accuracy_history = []
		self.validation_accuracy_history = []

		self.validation_error_history = np.zeros(epochs)
		self.validation_prediction_history = dict()

		if self.hidden_layer_weights.shape[0] != self.training_data.shape[1]:
			print("weight rows: ", self.hidden_layer_weights.shape[0])
			print("training_data cols: ", self.training_data.shape)
			raise Exception("The numbers of rows in the weights matrix does not match the number of columns " +
			                "in the training data matrix. Ensure that weights matrix contains a weight value for bias")

		if self.training_data.shape[1] != self.validation_data.shape[1]:
			print("training columns: ", self.training_data.shape[1])
			print("validation columns: ", self.validation_data.shape[1])
			raise Exception("The number of columns in the training data matrix does not match the number of columns"
			                + " in the valdiation data matrix")

	# Def rename to train
	def train(self):
		"""
		:return: i - number of epochs actually ran, training accuracy, validation accuracy
		"""
		_prev_accuracy = -sys.maxsize


		for i in range(0, self.epochs):
			self.training_confusion_matrix = np.zeros((self.output_node_count, self.output_node_count))
			self.validation_confusion_matrix = np.zeros((self.output_node_count, self.output_node_count))
			self.training_cycle()

			# get activations(as sigmoids) for data examples using final weights from previous training cycle
			training_output_activations = self.forward_propogate_all(self.training_data)
			for element_index in range(training_output_activations.shape[0]):
				_training_actual = np.argmax(training_output_activations[element_index])
				_training_target = (np.where(self.training_labels[element_index] == 0.9)[0])[0]  # =[t] without last [0]
				self.training_confusion_matrix[_training_target, _training_actual] += 1
				self.training_error_history[i] = putil.sum_squared_error(_training_target, _training_actual)

			test_output_activations = self.forward_propogate_all(self.validation_data)
			for element_index in range(test_output_activations.shape[0]):
				_test_prediction = np.argmax(test_output_activations[element_index])
				_test_target = np.where(self.validation_labels[element_index] == 0.9)[0][0]
				self.validation_prediction_history[i] = {
					"control string": self.validation_data[element_index][10:-1],  # split of bias input
					"datum ": self.validation_data[element_index][0:10],
					"predicted": _test_prediction,
					"actual": _test_target,
					"test_labels fill": self.validation_labels[element_index]
				}
				self.validation_confusion_matrix[_test_prediction, _test_target] += 1
			_curr_training_accuracy = putil.compute_accuracy(self.training_confusion_matrix)
			_validation_accuracy = putil.compute_accuracy(self.validation_confusion_matrix)
			self.training_accuracy_history.append(_curr_training_accuracy)
			self.validation_accuracy_history.append(_validation_accuracy)

			if i % 50 == 0:
				print("finished epoch ", i)
			if _validation_accuracy - _prev_accuracy < .000001 and _validation_accuracy > 0.95:
				self.epochs = i + 1  # update count for number of epochs actually ran - epoch counts start from 0
				break
			_prev_accuracy = _validation_accuracy
		return self.epochs, _curr_training_accuracy, _validation_accuracy

	def predict(self, data, data_labels):
		#TODO: return prediction dict, and confusion matrix

		output_activations = self.forward_propogate_all(data)
		print("output activations")
		print(output_activations.shape)
		predictions = np.argmax(output_activations, axis=1) # max columns
		confusion_matrix = np.zeros((self.output_node_count, self.output_node_count))
		#TODO: reshape from [1 x n] to [
		print("test predictions")      #TODO: test
		print(predictions)
		print(predictions.shape)
		print("labels shape")
		print(data_labels.shape)
		print(data_labels)
		history = dict()
		for element_index in range(output_activations.shape[0]):
			predicted = np.argmax(output_activations[element_index])
			target = (np.where(data_labels[element_index] == 0.9)[0])[0]  # =[t] without last [0]
			history[element_index] = {
				"predicted": predicted,
				"target": target
			}
			confusion_matrix[target, predicted] += 1
		return history, confusion_matrix

	def compute_accuracy(self, confusion_matrix):
		return putil.compute_accuracy(confusion_matrix)

	def display_training_prediction_history(self):
		print("training accuracy history: ", self.training_accuracy_history)
		print("validation accuracy history: ", self.validation_accuracy_history)

	def plot_accuracy_history(self, filename):
		self.display_training_prediction_history()
		print("history train count - y axis ", len(self.training_accuracy_history))
		print("history test count - y axis", len(self.validation_accuracy_history))
		print("Accuracy Histories: ")
		epochs = np.arange(self.epochs)  # turn into an array [1 x epoch_count]
		plt.plot(epochs, self.training_accuracy_history)
		plt.plot(epochs, self.validation_accuracy_history)
		plt.xlabel('epoch')
		plt.ylabel('accuracy')
		plt.legend(['training data', 'validation data'], loc='upper left')
		plt.savefig(filename)
		plt.clf()

	def plot_error_history(self):
		print("Error Histories: ")
		epochs = np.arange(self.epochs)  # turn into an array [1 x epoch_count] #histories start counting from 0
		plt.plot(epochs, self.training_error_history)
		plt.plot(epochs, self.validation_error_history)
		plt.xlabel('epoch')
		plt.ylabel('error')
		plt.legend(['training data', 'validation data'], loc='upper left')
		plt.show()
		plt.savefig
		plt.clf()

	def save_final_results(self, filename):
		"""
			writes the final accuracies and confusion matrices to a file
		"""
		file = open(filename, "w")

		file.write("Neural Network with " + str(self.hidden_node_count) + " hidden nodes and momentum " +
		           str(self.momentum) + " had a final training accuracy of " +
		           str(self.training_accuracy_history[self.epochs - 1]) + "\n and a test accuracy of " +
		           str(self.validation_accuracy_history[self.epochs - 1]) + " after " + str(self.epochs) + " epochs")
		file.write("\nTest Confusion Matrix: \n")
		file.write(str(self.validation_confusion_matrix))
		file.write("\ntraining accuracy history: \n" + str(self.training_accuracy_history))
		file.write("\nvalidation accuracy history: \n" + str(self.validation_accuracy_history))
		file.close()

	def training_cycle(self):
		output_prev_delta = np.zeros(np.shape(self.output_layer_weights))
		hidden_prev_delta = np.zeros(np.shape(self.hidden_layer_weights))
		input_list = np.arange(self.training_data.shape[0])  # fills list with values 0 to n; n is size of train set
		np.random.shuffle(input_list)  # randomize order - list entries are used to determine next datum for training
		for i in range(self.training_data.shape[0]):  # tune weights after each training example in training data set
			data_example_index = input_list[i]
			_hidden_layer_activations, _output_layer_activations = self.forward_propagate(
				self.training_data[data_example_index])
			_target_activations = self.training_labels[data_example_index]

			"""calculate the error term for each output term k.  Shape[ 1 x 10] because we have 10 output nodes"""
			delta_o_values = _output_layer_activations * (1.0 - _output_layer_activations) * (
					_output_layer_activations - _target_activations)

			"""Calculate the error terms for hidden layers  bias" """  # slides Lecture 6 pg 37
			# shape = [1 x n] * [n x m] = [1 x m]   but the last value will be zero -- this is for the bias
			delta_h_inner = np.dot(delta_o_values, self.output_layer_weights.T)  # needs to come before the weight
			# updates
			delta_h_values = _hidden_layer_activations * (1.0 - _hidden_layer_activations) * delta_h_inner

			""" updated output layer weights = Dwkj + momentum * previous weight change """
			# Dwkj = h*(d_k)*(h_j) where h is the learning rate, d_k = the error lose for node output node k &
			# hj = activation for hidden node j
			output_prev_delta = self.learning_rate * np.dot(_hidden_layer_activations.T,
			                                                delta_o_values) + self.momentum * output_prev_delta

			# shape: [1 x input node count]
			data_example = np.reshape(self.training_data[data_example_index],
			                          (1, self.training_data[data_example_index].shape[0]))

			# Dwji shape is [input node count x hidden layer count ] = [ipc x 1] * [1 x hlc] - stripped off bias
			hidden_prev_delta = self.learning_rate * np.dot(data_example.T,
			                                                delta_h_values[:, :-1]) + self.momentum * hidden_prev_delta

			self.hidden_layer_weights -= hidden_prev_delta
			self.output_layer_weights -= output_prev_delta

	def forward_propogate_all(self, data_examples_set):
		"""
		:param data_examples_set: data_examples_set should already have a bias node appended to inputs
		:return: hidden_layer_sigmoids shape: [n x hidden node count + 1 bias node]
				 output_layer_sigmoids shape: [n x output node count]
				where n is number of training examples in data_set
		"""
		hidden_layer_activations = np.dot(data_examples_set, self.hidden_layer_weights)
		hidden_layer_sigmoids = putil.sigmoid_activation_values_all(hidden_layer_activations)

		_hidden_bias_col = np.ones((np.shape(hidden_layer_sigmoids)[0], 1))
		hidden_layer_sigmoids = np.append(hidden_layer_sigmoids, _hidden_bias_col, axis=1)

		output_layer_activations = np.dot(hidden_layer_sigmoids, self.output_layer_weights)
		output_layer_sigmoids = putil.sigmoid_activation_values_all(output_layer_activations)
		return output_layer_sigmoids

	def forward_propagate(self, data_example):
		"""
		:param data_example:
		:return: hidden layer activations includes all the input values + the bias -- shape: [1x20] where each
		column represents the sigmoid activation for the kth hidden node

			output layer activation
		"""
		# [1 example x input node count] * [input node count x hidden node count]  = [1 x hidden note count activations]
		# each column represents the activation value for node k
		data_example = np.reshape(data_example, (1, len(data_example)))

		# shape: [ipc x hnc]
		hidden_layer_activations = np.dot(data_example, self.hidden_layer_weights)

		# use sigmoid to squash activation value for each node k for every data example = [dataset size x hnc]
		hidden_layer_sigmoids = putil.sigmoid_activation(hidden_layer_activations)

		# add bias  so that inputs into output layer is hdc hidden layer activations + (1 bias)
		hidden_layer_sigmoids = np.concatenate((hidden_layer_sigmoids,
		                                        np.ones((np.shape(hidden_layer_sigmoids)[0], 1))),
		                                       axis=1)

		# [1 x (hidden node count + 1bias)] * [(hidden node count + 1bias) x n output nodes] = [1 x n ]
		# each col is activation for output node k
		output_layer_activations = np.dot(hidden_layer_sigmoids, self.output_layer_weights)
		output_layer_sigmoids = putil.sigmoid_activation(output_layer_activations)
		return hidden_layer_sigmoids, output_layer_sigmoids
