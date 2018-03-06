import random
import binarycreator
import hammingdistanceclassifier.hammingdatagenerator as hdg
import hammingdistanceclassifier.hdcrunner as hdcrunner
import sys


def main():
	# create random string
	# make training data from string
	if sys.argv.__contains__("-bc"):
		random_decimal = random.randrange(256, 516)
		binarycreator.create_and_classify_binary_set("rgflclassifier/random-binary.txt", random_decimal)


	#TODO: add sys arg
	# train data model.
	# if sys.argv.__contains__("-hdg"):
	hdg.create_data(10, 1000, "hammingdistanceclassifier/hammingdata.csv")

	hdcrunner.run()



if __name__ == '__main__':
	main()
