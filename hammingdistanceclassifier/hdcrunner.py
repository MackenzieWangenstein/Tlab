import pandas as pd
import numpy as np


def run():
	control_str = np.genfromtxt('hammingdistanceclassifier/control_str.csv')
	print(control_str)
	class_count = control_str.shape[0]
	hamming_dist_dataset = pd.read_csv("hammingdistanceclassifier/hammingdataall.csv").values
	print(hamming_dist_dataset)
	#10s class
	tens = hamming_dist_dataset[hamming_dist_dataset[:, class_count] == 10]
	print(tens)


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





