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
	:param control_dataset:
	:return:
	"""
	total_size = control_dataset.shape[0]
	train_size = math.ceil(total_size /2)   #more training  => better
	test_size = math.ceil((total_size - train_size)/2)
	validation_size = total_size - test_size - train_size

	if train_size + test_size + validation_size != total_size:
		print("partitioned sets don't add up to size of training")
		print("total size: ", total_size)
		print("size of all ", train_size + test_size + validation_size)
		print("train: ", train_size)
		print("test size: ", test_size)
		print("validation size: ", validation_size)
	else:
		print("partitioned sets do  add up to size of training")
		print("total size: ", total_size)
		print("size of all ", train_size + test_size + validation_size)
		print("train: ", train_size)
		print("test size: ", test_size)
		print("validation size: ", validation_size)


	# for i in range(class_count)

