import copy


def create_and_classify_binary_set(filename, decimal_num):
    file = open(filename, "w")
    mutated_set = []
    non_mutated_set = []


    training_binary = '{0:b}'.format(decimal_num)
    #training_binary = format(decimal_num, 'b')

    training_binary_len = len(training_binary)
    print("Training String: " + training_binary)


    # create binary representations of all the decimals numbers whose binary values have the same length as the training
    # string -- except for training string
    last_dec_in_range = pow(2, training_binary_len)
    for i in range(pow(2, training_binary_len - 1) + 1, last_dec_in_range):
        binary_string = convert_to_data_format(training_binary, training_binary_len, '{0:b}'.format(i))
        if i != last_dec_in_range:
            binary_string = binary_string + "\n"
        file.write(binary_string)
    file.close()


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


def convert_to_data_format(training_binary, training_bin_len, src_binary):
    """ Appends commas between characters and appends a 1 or 0 to the end of the string.
     1 indicates that the src binary is a mutated version of the training binary.
     example: 100000000 -> 1,0,0,0,0,0,0,0,0,1 where training bin = 000000000"""
    if training_bin_len != len(src_binary):
        return Exception("Source string and training string must be the same length!")
    formatted_string = ""
    mutated_pos_count = 0;
    for i in range(0, training_bin_len):
        formatted_string = formatted_string + src_binary[i] + ','
        if training_binary[i] != src_binary[i]:
            mutated_pos_count = mutated_pos_count + 1
    if mutated_pos_count == 1:
        formatted_string = formatted_string + '1'
    else:
        formatted_string = formatted_string + '0'
    print(formatted_string)
    return formatted_string

# def test(){
    #
    # #.replace()a
    # #    print(format(trainingBin, ',str'))
    # print("compBin: ", trainingBin)
    #
    # # print("length", trainingBinLength)
    # fileString = ""
    #
    # print(fileString)
    #
    # mutatedString = '100000001'
    # print("testing conversion of muated string ,", mutatedString," match expected!")
    # convertToDataFormat(trainingBin, trainingBinLength, mutatedString)
    #
    # mutStringToPad = '1000'
    # updatededStr = padString(trainingBinLength, mutStringToPad)
    # print("testing conversion of padded-mutated string ,", updatededStr, " match  expected!")
    # convertToDataFormat(trainingBin, trainingBinLength, updatededStr)
    #
    # nonMutatedString = '100001111'
    # print("testing conversion of non-mutated string ,", nonMutatedString, " match not expected!")
    # convertToDataFormat(trainingBin, trainingBinLength, nonMutatedString)

# }
