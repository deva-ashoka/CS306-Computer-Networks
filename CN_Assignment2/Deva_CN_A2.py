# Computer Networks: Assignment 2 - Noisy binary channel
# Name: Deva Surya Vivek

import sys
import random


def generateRandomlyWithProb(p):
    num = random.uniform(0.0, 1.0)
    if num <= p:
        return 1
    else:
        return 0


if len(sys.argv) == 2:
    fileName = sys.argv[1]
    inputLines = [line.rstrip('\n') for line in open(fileName)]

    p = float(inputLines[0])
    if p < 0 or p > 1:
        print("Error: probability has to be in the range (0,1)")
    else:
        x = inputLines[1]

        length = len(x)
        xor = ""

        for i in range(length):
            xor += str(generateRandomlyWithProb(p))

        y = ""
        for i in range(length):
            y += str((int(x[i]) ^ int(xor[i])))

        print("p = " + str(p))
        print("x = " + x)
        print("y = " + y)
else:
    print("Invalid arguments! Try: $ python file_name.py input.txt")
