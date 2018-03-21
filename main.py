import random
import binarycreator
import hammingdistanceclassifier.hammingdatagenerator as hdg
import hammingdistanceclassifier.hdcrunner as hdcrunner
import sys


def main():
	if sys.argv.__contains__("-bc"):
		random_decimal = random.randrange(256, 516)
		binarycreator.create_and_classify_binary_set("rgflclassifier/random-binary.txt", random_decimal)

	if sys.argv.__contains__("-hdgen"):
		hdg.create_data(10, 1000, "hammingdistanceclassifier/hammingdata.csv")

	if sys.argv.__contains__("-hdc"):
		hdcrunner.run()


if __name__ == '__main__':
	main()