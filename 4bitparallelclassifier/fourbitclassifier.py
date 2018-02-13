import pandas as pd
import numpy as np
"""
    The goal of this classifier is to feed in two 4bit strings in order to detect if the second string is a
    mutated version of the first string

    first string, randomly generated 2

    example: string_1 = 0101
           : string_2 = 1101
             expected_output: 1

             string_1 = 0101
             string_2 = 0101
             expected_output: 1

             string_1 = 1111
             string_2 = 0101
             expected_output: 2

        input_nodes: 8
        output_node: 1


"""
class  FourBitClassifier(object):
    #step 1: randomly generate a number x where 16 <=x < 32 to ensure a binary string of length 4 is generated,
    def get_random(self):
        print("place holder")


    # #step 2: create training_set  -- according to Dr. Teuscher it is okay for the training data to have repeat values
    # #generate a thousand strings where bits are arbitrary chosen to flip
    def createTrainingSet(self, ):
        print("place holder")



    #step 3: create test set