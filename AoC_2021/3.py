
def convert(string):
    retval = 0
    string = string[::-1]
    print(string)
    for index, char in enumerate(string):
        retval += int(char) * (2**index)
    return retval

def mostCommon(index, arr):
    ones = [x[index] for x in arr].count("1")
    zeroes = [x[index] for x in arr].count("0")
    return '1' if ones >= zeroes else '0'

with open("3.txt", "r") as f:
    arr = f.read().split("\n")

    probs = [{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0},{'0':0, '1':0}]

    for binaryReadout in arr:
        for count, bit in enumerate(binaryReadout):
            probs[count][bit] += 1

    print(probs)

    gamma = ''.join(['1' if dictio['1'] > dictio['0'] else '0' for dictio in probs])

    epsilon = ''.join(['1' if dictio['1'] < dictio['0'] else '0' for dictio in probs])

    gammaInt = convert(gamma)
    epsilonInt = convert(epsilon)

    print("Part 1:", gammaInt * epsilonInt)


    #oxygen level
    oxygenlist = [i for i in arr]
    for index in range(12):
        print(index)
        for binaryReadout in arr:
            if mostCommon(index, arr) != binaryReadout[index]:
                oxygenlist.remove(binaryReadout)
    
    print(oxygenlist)
    print(arr)
