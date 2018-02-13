import random
import binarycreator
import hammingdistanceclassifier.hammingdatagenerator as hdg
import sys


def main():
	# create random string
	# make training data from string
	if sys.argv.__contains__("-bc"):
		random_decimal = random.randrange(256, 516)
		binarycreator.create_and_classify_binary_set("rgflclassifier/random-binary.txt", random_decimal)

	# train data model.
	hdg.create_data(10, 100, "hammingdistanceclassifier/hammingdata.csv")



if __name__ == '__main__':
	main()
