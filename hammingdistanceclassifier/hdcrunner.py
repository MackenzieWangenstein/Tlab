import pandas as pd
import numpy as np
import math

def run():
	control_str = np.genfromtxt('hammingdistanceclassifier/control_str.csv')
	print(control_str)
	class_count = control_str.shape[0]
	hamming_dist_dataset = pd.read_csv("hammingdistanceclassifier/hammingdataall.csv").values
	control_hamming_dist_dataset = np.array(hamming_dist_dataset)
	print(control_hamming_dist_dataset.shape, " control")

	print(hamming_dist_dataset)
	#10s class
	tens = hamming_dist_dataset[hamming_dist_dataset[:, class_count] == 10]
	print(tens)

	create_data_sets(control_hamming_dist_dataset, class_count)



	#figure out how to balance train, test and validate clas s-- equal representation for each?

	#half of each the data for each class goes to to training -- the other part gets split between test and validation


	# print(hamming_dist_dataset)
	# np.random.shuffle(hamming_dist_dataset) # TODO: will need to shuffle training dataset between epochs as well when
	# training
	#^^ if we do it this way though can we accurately compare models??? run two trials - one where set is the same
	# between trials - and another where we shuffle so that we do not constantly have the same data items in train set

	#split data between

	# hd_dataset = hamming_dist_dataset[:, 0:class_count]  # strip off labels
	# print(hd_dataset.shape)

	# hd_dataset_labels = hamming_dist_dataset[:, class_count] # collect labels - strip off labels after splitting
# into tests
	# print(hd_dataset_labels.shape)
	#





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

		print("\n")

	print("training data shape after: ", training_data.shape)
	print("test data shape after: ", test_data.shape)
	print("val data shape after: ", validation_data.shape)


