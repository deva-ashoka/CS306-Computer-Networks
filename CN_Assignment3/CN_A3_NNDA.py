# CN Assignment 3
# Name: Deva Surya Vivek

import sys


def padZeroes(string, size):
    length = len(string)
    if length < size:
        numOfZeroes = size - length
        for i in range(0, numOfZeroes):
            string = '0' + string
    return string


if len(sys.argv) == 2:
    fileName = sys.argv[1]
    inputLines = [line.rstrip('\n') for line in open(fileName)]

    k = int(inputLines[0].split(',')[0])
    n = int(inputLines[0].split(',')[1])
    p = float(inputLines[1])

    del (inputLines[0])
    del (inputLines[0])

    print("k = " + str(k))
    print("n = " + str(n))
    print("p = " + str(p))

    H = [[0 for col in range(0, n)] for ro in range(0, n - k)]

    print("H = ")

    for i in range(0, n - k):
        j = 0
        for element in inputLines[i]:
            H[i][j] = int(element)
            j += 1

    for row in H:
        print ' '.join(map(str, row))

    for i in range(0, n - k):
        del (inputLines[0])

    y = inputLines[0]

    print("y = " + y)

    possibleStrings = []
    minDistance = n

    for num in range(0, 2 ** k):

        binaryString = "{0:b}".format(num)
        binaryString = padZeroes(binaryString, k)

        codeWordTemp = ''
        for row in H:
            temp = 0
            for i in range(0, k):
                temp += int(row[i]) * int(binaryString[i])
            temp %= 2
            codeWordTemp += str(temp)
        codeWord = binaryString + codeWordTemp

        distance = 0
        for i in range(0, n):
            distance += int(codeWord[i]) ^ int(y[i])

        if distance == minDistance:
            possibleStrings.append(codeWord)
        if distance < minDistance:
            del possibleStrings[:]
            possibleStrings.append(codeWord)
            minDistance = distance

    print("------------------------")
    print("Possible Strings of x = ")
    print(possibleStrings)
    print("Minimum Distance = " + str(minDistance))
    outputFile = open("output.txt", 'w')
    for string in possibleStrings:
        outputFile.write(string + "\n")
else:
    print("Invalid arguments! Try: $ python file_name.py input.txt")
