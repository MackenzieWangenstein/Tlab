import numpy as np
import random
# take length of parameter --


def create_data(string_length, desired_dataset_size, filename):
	"""
	creates a control binary string of length n that is composed using a discrete unform form distribution,
		:param string_length, desired_dataset_size, filename:
	:return: control string, data set generated from string
	"""
	if desired_dataset_size < string_length:
		raise Exception("The desired dataset size is less than the number of hamming distance classes that exist for a "
		                + "\nstring of this length. We could just make a dataset that would be meet this need but we "
		                  "\nbelief in transparancy. Please ensure that the desired number of training examples "
		                  "\nexceeds the desired length of the control string")

	# create control string
	control_str = np.random.randint(2, size=string_length)


	# ensure that tions exist for each possible hemming distance class from 0 to len(control string)

	# randomly
	return control_str


