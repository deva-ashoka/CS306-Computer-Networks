import random


def squareNMultiply(x, c, n):
    c1 = bin(c).lstrip('0b')
    c2 = []
    for bit in c1:
        c2.append(int(bit))
    c2.reverse()
    l = len(str(bin(c).lstrip('0b')))
    z = 1
    for i in range(l - 1, -1, -1):
        z = (z ** 2) % n
        if c2[i] == 1:
            z = (z * x) % n
    return z


def rabinMiller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % num
    return True


def primegenerator(n):
    count = 0
    for i in range(0, 20):
        x = rabinMiller(n)
        if x:
            count += 1
    if count == 20:
        return n
    else:
        return -1


def setup():
    bitLength = 100

    p = 0
    q = 0

    itr1 = True
    itr2 = True

    while itr1:
        randomNum = random.randint(2 ** (bitLength - 1), 2 ** bitLength)
        if randomNum % 2 == 0:
            itr1 = True
        else:
            prime = primegenerator(randomNum)
            if prime != -1:
                p = randomNum
                itr1 = False

    while itr2:
        randomNum = random.randint(2 ** (bitLength - 1), 2 ** bitLength)
        if randomNum % 2 == 0:
            itr2 = True
        else:
            prime = primegenerator(randomNum)
            if prime != -1:
                q = randomNum
                itr2 = False

    n = p * q

    a1 = random.randint(0, n - 1)
    a2 = random.randint(0, n - 1)
    a3 = random.randint(0, n - 1)

    b1 = squareNMultiply(a1, 2, n)
    b2 = squareNMultiply(a2, 2, n)
    b3 = squareNMultiply(a3, 2, n)

    f = open("a1.txt", 'w')
    f.write(str(a1))
    f.close()

    f = open("a2.txt", 'w')
    f.write(str(a2))
    f.close()

    f = open("a3.txt", 'w')
    f.write(str(a3))
    f.close()

    f = open("n.txt", 'w')
    f.write(str(n))
    f.close()

    entries = list()
    entries.append(['Name-1', [b1, n]])
    entries.append(['Name-2', [b2, n]])
    entries.append(['Name-3', [b3, n]])

    return entries
