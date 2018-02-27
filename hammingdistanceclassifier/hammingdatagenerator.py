import numpy as np
import binarycreator

import random
# take length of parameter --

#TODO: consider refactoring to class

def create_data(string_length, desired_dataset_size, filename):
	"""
	creates a control binary string of length n that is composed using a discrete uniform form distribution,
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
	print("control str ", control_str)
	# create_and_classify_binary_with_binary(filename, control_str)
	create_training_data(filename, control_str, desired_dataset_size)

	# ensure that tions exist for each possible hemming distance class from 0 to len(control string)



	# randomly
	return control_str


def create_training_data(filename, control_str, desired_dataset_size):
	"""
	Create training data where half of the data is randomly generated, and half the
	labels on training data is hamming distance between the controls str and the generated string for the data example
	:param filename:
	:param control_str:
	:param desired_dataset_size:
	:return:
	"""
	training_data = []
	# random_data = create_random_binary(len(control_str), desired_dataset_size/2)
	# training_data.append(random_data)
	mutation_data = create_random_mutations(control_str, int(desired_dataset_size/2))
	training_data.append(mutation_data)
	for i in range(len(training_data)):
		print("data example: ", training_data)
		#format string and write to file


#if problem with data -- ie classes are not distrubed equally - split # of training requirements / length of string
#to determine how many training examples should be in each class.

def create_random_mutations(control_str, desired_dataset_size):
	control_str_length = len(control_str)
	training_data = np.zeros((desired_dataset_size, control_str_length + 1))
	#shape m xn where m = # of training and makes space for training label

	for i in range(desired_dataset_size):
		mutated_str = np.copy(control_str)
		#randomly choose how many positions to flip
		num_of_pos_to_flip = np.random.randint(control_str_length, size=1)
		# randomly choose which positions where the digit should be flipped
		pos_to_flip = np.random.choice((control_str_length - 1), num_of_pos_to_flip, replace=False)
		for j in range(num_of_pos_to_flip[0]):
			print("pos to flip: ", pos_to_flip[j])
			if mutated_str[pos_to_flip[j]] == 1:
				mutated_str[pos_to_flip[j]] = 0
			else:
				mutated_str[pos_to_flip[j]] = 1
		mutated_str = np.append(mutated_str, num_of_pos_to_flip)
		training_data[i] = mutated_str
	return training_data


# other half of the data is randomly created strings
def create_random_binary(control_str_length, desired_training_size):
	training_data = np.zeros((desired_training_size, control_str_length))  #shape m xn where m = # of training example
	for i in range(desired_training_size):
		generated_str = np.zeros(control_str_length)
		#randomly choose how many positions to flip
		num_of_pos_to_flip = np.random.randint(control_str_length, size=1)
		# randomly choose which positions where the digit should be flipped
		pos_to_flip = np.random.choice((control_str_length - 1), num_of_pos_to_flip, replace=False)
		for j in range(num_of_pos_to_flip[0]):
			generated_str[pos_to_flip[j]] = 1
		training_data[i] = generated_str
	return training_data




# def create_and_classify_binary_with_binary(filename, training_binary):
#     file = open(filename, "w")
#
#     training_binary_len = len(training_binary)
#
#     # create binary representations of all the decimals numbers whose binary values have the same length as the training
#     # string -- except for training string
#     last_dec_in_range = pow(2, training_binary_len)
#     for i in range(pow(2, training_binary_len - 1) + 1, last_dec_in_range):
#         binary_string = convert_to_data_format(training_binary, training_binary_len, '{0:b}'.format(i))
#         if i != last_dec_in_range:
#             binary_string = binary_string + "\n"
#         file.write(binary_string)
#     file.close()

# def pad_string(training_binary_len, src_binary):
#     padded_string = src_binary.rjust(training_binary_len, '0')
#     print("padding string ", padded_string)
#     return padded_string


# def convert_to_data_format(control_training_binary, training_bin_len, mutated_binary):
#     """ Appends commas between characters and appends a 1 or 0 to the end of the string.
#      1 indicates that the src binary is a mutated version of the training binary.
#      example: 100000000 -> 1,0,0,0,0,0,0,0,0,1 where training bin = 000000000"""
#     if training_bin_len != len(mutated_binary):
#         return Exception("Source string and training string must be the same length!")
#     formatted_string = ""
#     mutated_pos_count = 0
#     print("inside convert data --str length ", training_bin_len)
#     for i in range(0, training_bin_len):
#         formatted_string = formatted_string + mutated_binary[i] + ','
#         if control_training_binary[i] != str(mutated_binary[i]):
# 	        print("updated mutated pos count: control trainin bin[i] = ", control_training_binary[i], "mutated binary[i]= ", mutated_binary[i])
# 	        mutated_pos_count = mutated_pos_count + 1
#     print("mutated pos count", mutated_pos_count)
#     formatted_string = formatted_string + str(mutated_pos_count)
#     print("Final mutation count between control string ", control_training_binary, " and mutated string ",
#           mutated_binary, " is ", mutated_pos_count)
#     return formatted_string



