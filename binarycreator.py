import copy
# todo: convert number to convert to binary as trainingBin to be a parameter instead of being hardcoded
def createAndClassify():
    file = open("generatedBinary.txt", "w")
    trainingBin = '{0:b}'.format(256)
    trainingBinLength = len(trainingBin)

    #add first mutation
    firstMutation = copy.copy(trainingBin)
    if firstMutation[0] == '0':
        firstMutation = '1' + firstMutation[1:]
    else:
        firstMutation = '0' + firstMutation[1:]
    firstMutation = convertToDataFormat(trainingBin, trainingBinLength, firstMutation)
    file.write(firstMutation)

    #TODO: change logic when replacing hard en
    #256   = 2^8.     generater numbers from 257  to  512(2^9)-1) and convert to binary
    for i in range(257, 512):
        binarySring = '{0:b}'.format(i)
        file.write(convertToDataFormat(trainingBin, trainingBinLength, binarySring)+'\n')

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

    file.close()

    # file.write(trainingBin)
    # file.close()
    # for i in range(0, 255):
    #     file.write(i.)


def padString(trainingBinLen, srcBin):
    paddedString = srcBin.rjust(trainingBinLen, '0')
    print("padding string ", paddedString)
    return paddedString;


# example: 100000000 -> 1,0,0,0,0,0,0,0,0
def convertToDataFormat(trainingBin, trainingBenLen, srcBin):
    if trainingBenLen != len(srcBin):
        return Exception("Src string and training string must be the same length!")
    fileString = ""
    mutatedPosCount = 0;
    for i in range(0, trainingBenLen):
        fileString = fileString + srcBin[i]
        fileString = fileString + ','
        if trainingBin[i] != srcBin[i]:
            mutatedPosCount = mutatedPosCount + 1
    if (mutatedPosCount <= 1):
        fileString = fileString + '1';  # might need to convert to string
    else:
        fileString = fileString + '0'
    print("converted string: ", fileString)
    return fileString
