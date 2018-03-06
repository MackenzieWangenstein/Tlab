import numpy as np
import pandas as pd
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
	control_str = np.reshape(control_str, (1, control_str.shape[0]))
	print(control_str.shape)
	np.savetxt("hammingdistanceclassifier/control_str.csv", control_str, fmt='%1d')
	print("control str ", control_str[0])

	# create_and_classify_binary_with_binary(filename, control_str)
	create_training_data(filename, control_str[0], desired_dataset_size)  #TODO: is this why 10's aren't being found

	# ensure that tions exist for each possible hemming distance class from 0 to len(control string)
	return control_str

#TODO: figure out why 10 mutation is not occuring
def create_training_data(filename, control_str, desired_dataset_size):
	mutation_data = create_random_mutations_balanced(control_str, desired_dataset_size)
	np.savetxt("hammingdistanceclassifier/hammingdataall.csv", mutation_data, fmt='%1d', delimiter=',')


def create_training_data_mixed(filename, control_str, desired_dataset_size):
	"""
	Create training data where half of the data is randomly generated, and half the
	labels on training data is hamming distance between the controls str and the generated string for the data example
	:param filename:
	:param control_str:
	:param desired_dataset_size:
	:return:
	"""
	mutated_data_size = int(desired_dataset_size/2)
	print("mudated data size ", mutated_data_size)
	mutation_data = create_random_mutations_balanced(control_str, mutated_data_size)
	print("mutation data")
	print(mutation_data)
	random_data_size = desired_dataset_size - mutated_data_size
	print("random data size", random_data_size)
	random_data = create_random_binary(len(control_str), random_data_size)
	print("random data")
	print(random_data)
	training_data = np.row_stack((random_data, mutation_data))
	print(training_data.shape)
	np.savetxt("hammingdistanceclassifier/hammingdataall.csv", training_data, fmt='%1d', delimiter=',')


#if problem with data -- ie classes are not distrubed equally - split # of training requirements / length of string
#to determine how many training examples should be in each class.

def create_random_mutations_unbalanced(control_str, desired_dataset_size):
	control_str_length = len(control_str)
	training_data = np.zeros((desired_dataset_size, control_str_length + 1))
	for i in range(desired_dataset_size):
		num_of_pos_to_flip = np.random.randint(control_str_length, size=1)
		training_data[i] = create_mutated_string(np.array(control_str), num_of_pos_to_flip[0])
	return training_data


def create_mutated_string(mutated_str, num_of_pos_to_flip):
			#generate n copies of random number from 0 to # of max hamming distance
	pos_to_flip = np.random.choice(len(mutated_str), num_of_pos_to_flip, replace=False)
	for j in range(num_of_pos_to_flip):
		if mutated_str[pos_to_flip[j]] == 1:
			mutated_str[pos_to_flip[j]] = 0
		else:
			mutated_str[pos_to_flip[j]] = 1
	mutated_str = np.append(mutated_str, num_of_pos_to_flip)
	return mutated_str


#class = hamming distance  o(n^3) :(
def create_random_mutations_balanced(control_str, desired_dataset_size):
	control_str_length = len(control_str)
	training_data = np.zeros((desired_dataset_size, control_str_length + 1))
	data_index = 0

	# Ensurs data classes are balanced in training data example
	count_per_class = int(desired_dataset_size/len(control_str))

	#skip for class = 0 , just append count_per_class copys of control_str to training data to account for it
	for class_value in range(1, control_str_length + 1):
		# create n random training examples for specified class
		#was going to attempt to use random choice with shape =2d instead of 1d to avoid 3 loops - wont work 4 w/o repl.
		for i in range(0, count_per_class):
			mutated_str = create_mutated_string(np.array(control_str), class_value)
			training_data[data_index] = mutated_str
			data_index += 1

	# create remaining daa
	for j in range(data_index, desired_dataset_size):
		num_of_pos_to_flip = np.random.randint(control_str_length, size=1)
		mutated_str = create_mutated_string(np.array(control_str), num_of_pos_to_flip[0])
		training_data[j] = mutated_str

	return training_data;

# other half of the data is randomly created strings
def create_random_binary(control_str_length, desired_training_size):
	training_data = np.zeros((desired_training_size, control_str_length + 1))  #shape m xn where m = # of training
	# example
	for i in range(desired_training_size):
		generated_str = np.zeros(control_str_length)
		#randomly choose how many positions to flip
		num_of_pos_to_flip = np.random.randint(control_str_length, size=1)
		pos_to_flip = np.random.choice((control_str_length), num_of_pos_to_flip, replace=False)
		for j in range(num_of_pos_to_flip[0]):
			generated_str[pos_to_flip[j]] = 1
		training_data[i] = np.append(generated_str, num_of_pos_to_flip[0])
	return training_data