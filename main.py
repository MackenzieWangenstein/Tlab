import random
import binarycreator
import hammingdistanceclassifier.hammingdatagenerator as hdg
import hammingdistanceclassifier.hdcrunner as hdcrunner
import sys
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--binary_creator', '-bc', help='create and classify binary set', action='store_true')
	parser.add_argument('--hamming_data_generator', '-hdgen', help='creates hamming distance data',
	                    action='store_true')
	parser.add_argument('--hamming dist runner', '-hdr', help='runs a classifier that predicts hamming distance '
	                                                          'count', action='store_true')
	parser.add_argument('--momentum', '-m', action='store_const', const=0.9)
	parser.add_argument('--learning_rate', '-rl', action='store_const', const=0.01)
	parser.add_argument('--hidden_node_count', '-hn', action='store_const', const=20)
	parser.add_argument('--epoch', '-e', action='store_const', const=50)
	args = parser.parse_args()


	# if sys.argv.__contains__("-bc"):
	print(args)
	if args["-bc"]:
		random_decimal = random.randrange(256, 516)
		binarycreator.create_and_classify_binary_set("rgflclassifier/random-binary.txt", random_decimal)

	if args["-hdgen"]:
		hdg.create_data(10, 1000, "hammingdistanceclassifier/hammingdata.csv")

	if args["-hdr"]:
		hdcrunner.run(args)


if __name__ == '__main__':
	main()