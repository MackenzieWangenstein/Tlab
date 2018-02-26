import numpy as np
import binarycreator

import random
# take length of parameter --


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
	create_and_classify_binary_with_binary(filename, control_str)

	# ensure that tions exist for each possible hemming distance class from 0 to len(control string)



	# randomly
	return control_str


def create_and_classify_binary_with_binary(filename, training_binary):
    file = open(filename, "w")

    training_binary_len = len(training_binary)

    # create binary representations of all the decimals numbers whose binary values have the same length as the training
    # string -- except for training string
    last_dec_in_range = pow(2, training_binary_len)
    for i in range(pow(2, training_binary_len - 1) + 1, last_dec_in_range):
        binary_string = convert_to_data_format(training_binary, training_binary_len, '{0:b}'.format(i))
        if i != last_dec_in_range:
            binary_string = binary_string + "\n"
        file.write(binary_string)
    file.close()

def pad_string(training_binary_len, src_binary):
    padded_string = src_binary.rjust(training_binary_len, '0')
    print("padding string ", padded_string)
    return padded_string


def convert_to_data_format(control_training_binary, training_bin_len, mutated_binary):
    """ Appends commas between characters and appends a 1 or 0 to the end of the string.
     1 indicates that the src binary is a mutated version of the training binary.
     example: 100000000 -> 1,0,0,0,0,0,0,0,0,1 where training bin = 000000000"""
    if training_bin_len != len(mutated_binary):
        return Exception("Source string and training string must be the same length!")
    formatted_string = ""
    mutated_pos_count = 0
    print("inside convert data --str length ", training_bin_len)
    for i in range(0, training_bin_len):
        formatted_string = formatted_string + mutated_binary[i] + ','
        if control_training_binary[i] != str(mutated_binary[i]):
	        print("updated mutated pos count: control trainin bin[i] = ", control_training_binary[i], "mutated binary[i]= ", mutated_binary[i])
	        mutated_pos_count = mutated_pos_count + 1
    print("mutated pos count", mutated_pos_count)
    formatted_string = formatted_string + str(mutated_pos_count)
    print("Final mutation count between control string ", control_training_binary, " and mutated string ",
          mutated_binary, " is ", mutated_pos_count)
    return formatted_string



