import random
import binarycreator
import hammingdistanceclassifier.hammingdatagenerator as hdg
import hammingdistanceclassifier.hdcrunner as hdcrunner
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--binary_creator', '-bc', help='create and classify binary set', action='store_true')
	parser.add_argument('--hamming_data_generator', '-hdgen', help='creates hamming distance data',
	                    action='store_true')
	parser.add_argument('--hamming_dist_runner', '-hdr', help='runs a classifier that predicts hamming distance '
	                                                          'count', action='store_true')
	parser.add_argument('--momentum', '-m', type=float, default=0.9)
	parser.add_argument('--learning_rate', '-rl', type=float, default=0.01)
	parser.add_argument('--hidden_node_count', '-hdn', type=int, default=20)
	parser.add_argument('--epochs', '-e', type=int, default=50)
	parser.add_argument('--print_details', '-pd', action='store_true')
	args = parser.parse_args()


	# if sys.argv.__contains__("-bc"):
	print(args)
	print(args.binary_creator)
	if args.binary_creator:
		random_decimal = random.randrange(256, 516)
		binarycreator.create_and_classify_binary_set("rgflclassifier/random-binary.txt", random_decimal)

	if args.hamming_data_generator:
		hdg.create_data(10, 1000, "hammingdistanceclassifier/hammingdata.csv")

	if args.hamming_dist_runner:
		hdcrunner.run(args)


if __name__ == '__main__':
	main()