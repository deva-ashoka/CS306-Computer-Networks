# CN Assignment 3
# Name: Deva Surya Vivek

import sys
import numpy as np

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

    # Matrix H (n-k x n)
    H = [[0 for col in range(0, n)] for ro in range(0, n - k)]  # initializing the H matrix with all zeroes
    for i in range(0, n - k):
        j = 0
        for element in inputLines[i]:
            H[i][j] = int(element)
            j += 1
    print("H = ")
    for row in H:
        print ' '.join(map(str, row))

    for i in range(0, n - k):
        del (inputLines[0])

    # Matrix M (n x k)
    M = [[0 for col in range(0, k)] for ro in range(0, n)]  # initializing the M matrix with all zeroes
    for i in range(0, k):
        for j in range(0, k):
            if i == j:
                M[i][j] = 1
    for i in range(0, n - k):
        for j in range(0, k):
            M[i + k][j] = H[i][j]
    M = np.array(M)
    print("M = ")
    print(M)

    x = inputLines[0]
    if len(x) == k:
        print("x = " + str(x))
        x = np.array(list(x), dtype=int)
        print("-------------------------")
        y = np.dot(M, x)
        yString = ''
        for element in y:
            yString += str(element % 2)
        print("y = " + yString)
        outputFile = open("output.txt", 'w')
        outputFile.write(str(yString))
    else:
        print("Error: Invlaid string! Enter a string of length = " + str(k))
else:
    print("Invalid arguments! Try: $ python file_name.py input.txt")
