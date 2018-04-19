import pandas as pd
import numpy as np
import math
from neuralnet import NeuralNet
import pprint

def run(args):

	# leave in for testing ideas -- remove after : TODO:
	# momentum_zero = 0
	# momentum_quartile = 0.25
	# momentum_half = 0.50
	# hidden_nodes = 20
	# hidden_nodes_fifty = 50
	# hidden_nodes_hundred = 100
	# learning_rate = 0.01

	momentum_default = args.momentum
	epochs = args.epochs
	hidden_nodes = args.hidden_node_count
	learning_rate = args.learning_rate

	print(momentum_default, " Momentum")
	control_str = np.genfromtxt('hammingdistanceclassifier/control_str.csv')
	print(control_str)
	class_count = control_str.shape[0]
	hamming_dist_dataset = pd.read_csv("hammingdistanceclassifier/hammingdataall.csv").values
	control_hamming_dist_dataset = np.array(hamming_dist_dataset)
	label_pos = control_hamming_dist_dataset.shape[1] - 1

	''' Split dataset amongst train, test, and valdiation set'''
	train_data, test_data, validation_data = create_data_sets(control_hamming_dist_dataset, class_count)

	print("Shape of train data: ", train_data.shape)
	print("Shape of test data: ", test_data.shape)
	print("Shape of validation data: ", validation_data.shape)
	#TODO: add way to ensure no overlap between train and validation data - test and validation okay - look @ numpy



	''' Process Train set '''
	train_labels = train_data[:, label_pos]
	# append source str to each training string to feed source and training strings in parallel
	source_str_matrix = np.array([control_str, ] * train_data.shape[0])
	train_data = np.append(train_data[:, 0:label_pos], source_str_matrix, axis=1)
	# Strip off labels and append bias col(of 1s) to input values for training data
	train_data = np.append(train_data, np.ones((train_data.shape[0], 1)), axis=1)
	print("train data shape: ", train_data.shape)
	training_labels_matrix = np.full((train_data.shape[0], class_count + 1), .1)

	'''Create Test Set '''
	test_labels = test_data[:, label_pos]
	source_str_matrix = np.array([control_str, ] * test_data.shape[0])
	test_data = np.append(test_data[:, 0:label_pos], source_str_matrix, axis=1) #remove label + add src str
	test_data = np.append(test_data, np.ones((test_data.shape[0], 1)), axis=1) #add bias
	test_labels_matrix = np.full((test_data.shape[0], class_count + 1), .1)


	validation_labels = validation_data[:, label_pos]
	source_str_matrix = np.array([control_str, ] * validation_data.shape[0])
	validation_data = np.append(validation_data[:, 0:label_pos], source_str_matrix, axis=1)
	validation_data = np.append(validation_data, np.ones((validation_data.shape[0], 1)), axis=1)
	validation_labels_matrix = np.full((validation_data.shape[0], class_count + 1), .1)

	print("test valid data\n", validation_data)



	#TODO: come back
	# validation_data = np.append(validation_data[:, 0:label_pos], np.ones((validation_data.shape[0], 1)), axis=1)

	training_data_size = train_data.shape[0]
	test_data_size = test_data.shape[0]
	validation_data_size = validation_data.shape[0]

	for i in range(training_data_size):
		_train_target_output = int(train_labels[i])
		training_labels_matrix[i][_train_target_output] = 0.9

	test_labels_matrix = np.full((test_data_size, class_count + 1), 0.1)
	for j in range(test_data_size):
		_test_target_output = int(test_labels[j])
		test_labels_matrix[j][_test_target_output] = 0.9

	for k in range(validation_data_size):
		_validation_target_output = int(validation_labels[k])
		validation_labels

	run_experiment(hidden_nodes, learning_rate, momentum_default, class_count + 1, train_data,
	               training_labels_matrix, test_data, test_labels_matrix, epochs, "nn1", args)


#TODO: shuffle data
def create_data_sets(control_dataset, class_count):
	"""
		create training, test, and validation data sets
	"""
	label_pos = control_dataset.shape[1] - 1
	training_data = np.empty((0, control_dataset.shape[1]))
	test_data = np.empty((0, control_dataset.shape[1]))
	validation_data = np.empty((0, control_dataset.shape[1]))
	#for each class - split the data into training, test, and validation sets.
	for i in range(class_count+1):
		class_data = control_dataset[control_dataset[:, label_pos] == i, :]

		total_size = class_data.shape[0]
		train_size = math.ceil(total_size / 2)  # half the data goes to training because more training  => better
		test_size = math.ceil((total_size - train_size) / 2)  # split other half between val & test - test sz > vali. sz
		validation_size_ind = total_size - (total_size - test_size - train_size)

		class_train_data = class_data[:train_size, :]
		class_test_data = class_data[train_size:validation_size_ind, :]
		class_val_data = class_data[validation_size_ind:, :]

		training_data = np.append(training_data, class_train_data, axis=0)
		test_data = np.append(test_data, class_test_data, axis=0)
		validation_data = np.append(validation_data, class_val_data, axis=0)

	print("training data shape after: ", training_data.shape)
	print("test data shape after: ", test_data.shape)
	print("val data shape after: ", validation_data.shape)
	return training_data, test_data, validation_data


def run_experiment(hidden_nodes,
				   learning_rate,
				   momentum,
				   output_nodes,
				   training_data,
				   training_labels_matrix,
				   test_data,
				   test_labels_matrix,
				   epochs,
				   experiment_name,
                   args):
	nn = NeuralNet(hidden_nodes, learning_rate, momentum, output_nodes, training_data, training_labels_matrix,
				   test_data, test_labels_matrix, epochs, args.print_details)

	nn_epochs_ran, nn_training_accuracy, nn_test_accuracy = nn.run()
	print("test of training accuracy history in runner ");
	print("test of history list: ")
	for k in range(len(nn.training_accuracy_history)):
		print("history[", k, " :", nn.training_accuracy_history[k])
	nn.plot_accuracy_history("hammingdistanceclassifier/results/" + experiment_name + ".png")
	nn.save_final_results("hammingdistanceclassifier/results/" + experiment_name + ".txt")
	# nn.plot_error_history()
	print("Perceptron with momentum ", momentum, "and ", hidden_nodes, " hidden nodes had afinal training accuracy of ",
	      nn_training_accuracy, " and a test accuracy of ", nn_test_accuracy, "after ", nn_epochs_ran, " epochs")
	nn.display_prediction_history()
	pprint.pprint(nn.test_prediction_history)