import random
import binarycreator

def main():
    ## create random string
    # make training data from string
    random_decimal = random.randrange(256, 516)
        #random.sample(range(256, 516), 1)
    #train data on 256 _- todo: test
    print("random: ", random_decimal)
    binarycreator.create_and_classify_binary_set("rgflclassifier/random-binary.txt", random_decimal)

    # train datamodel.

if __name__ == '__main__':
    main()