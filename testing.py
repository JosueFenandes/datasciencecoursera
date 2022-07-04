from array import array


def findHighestNumber(array):
    highestNumber = 0
    for i in array:
        if i > highestNumber:
            highestNumber = i
    return highestNumber

