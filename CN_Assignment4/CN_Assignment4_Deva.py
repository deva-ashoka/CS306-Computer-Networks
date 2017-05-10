# Assignment 4: Simulate a network: hosts and self learning switches
# Name: Deva Surya Vivek
import sys

S1port2 = "H1"
S1port1 = "H2"
S2port3 = "H7"
S3port1 = "H5"
S3port3 = "H6"
S4port0 = "H4"
S4port2 = "H3"
S5port0 = "H8"
S5port3 = "H9"


def makeEntry(fileName, host, port):
    present = False
    entries = [entry.rstrip('\n') for entry in open(fileName)]

    for entry in entries:
        entryTokens = entry.split(",")
        entryHost = entryTokens[0]
        if entryHost == host:
            present = True
            break
    if not present:
        f = open(fileName, 'a')
        string = host + "," + port + "\n"
        f.write(string)


def port0OfS1(source, message, destination):
    S4("1", source, message, destination)


def port1OfS1(source, message, destination):
    print(S1port1 + " received message: " + message)


def port2OfS1(source, message, destination):
    print(S1port2 + " received message: " + message)


def port3OfS1(source, message, destination):
    S2("2", source, message, destination)


def S1(port, source, message, destination):
    switchFile = "S1.txt"
    makeEntry(switchFile, source, port)

    entries = [entry.rstrip('\n') for entry in open(switchFile)]
    entryAvailable = False
    entryPort = ""
    for entry in entries:
        entryTokens = entry.split(",")
        entryHost = entryTokens[0]
        entryPort = entryTokens[1]
        if entryHost == destination:
            entryAvailable = True
            break
    if entryAvailable:
        if entryPort == "0":
            port0OfS1(source, message, destination)
        elif entryPort == "1":
            port1OfS1(source, message, destination)
        elif entryPort == "2":
            port2OfS1(source, message, destination)
        elif entryPort == "3":
            port3OfS1(source, message, destination)
    else:
        if port != "0":
            port0OfS1(source, message, destination)
        if port != "1":
            port1OfS1(source, message, destination)
        if port != "2":
            port2OfS1(source, message, destination)
        if port != "3":
            port3OfS1(source, message, destination)


def port0OfS2(source, message, destination):
    return None


def port1OfS2(source, message, destination):
    S3("0", source, message, destination)


def port2OfS2(source, message, destination):
    S1("3", source, message, destination)


def port3OfS2(source, message, destination):
    print(S2port3 + " received message: " + message)


def S2(port, source, message, destination):
    switchFile = "S2.txt"
    makeEntry(switchFile, source, port)

    entries = [entry.rstrip('\n') for entry in open(switchFile)]

    entryAvailable = False
    entryPort = ""
    for entry in entries:
        entryTokens = entry.split(",")
        entryHost = entryTokens[0]
        entryPort = entryTokens[1]
        if entryHost == destination:
            entryAvailable = True
            break
    if entryAvailable:
        if entryPort == "0":
            port0OfS2(source, message, destination)
        elif entryPort == "1":
            port1OfS2(source, message, destination)
        elif entryPort == "2":
            port2OfS2(source, message, destination)
        elif entryPort == "3":
            port3OfS2(source, message, destination)
    else:
        if port != "0":
            port0OfS2(source, message, destination)
        if port != "1":
            port1OfS2(source, message, destination)
        if port != "2":
            port2OfS2(source, message, destination)
        if port != "3":
            port3OfS2(source, message, destination)


def port0OfS3(source, message, destination):
    S2("1", source, message, destination)


def port1OfS3(source, message, destination):
    print(S3port1 + " received message: " + message)


def port2OfS3(source, message, destination):
    return None


def port3OfS3(source, message, destination):
    print(S3port3 + " received message: " + message)


def S3(port, source, message, destination):
    switchFile = "S3.txt"
    makeEntry(switchFile, source, port)

    entries = [entry.rstrip('\n') for entry in open(switchFile)]

    entryAvailable = False
    entryPort = ""
    for entry in entries:
        entryTokens = entry.split(",")
        entryHost = entryTokens[0]
        entryPort = entryTokens[1]
        if entryHost == destination:
            entryAvailable = True
            break
    if entryAvailable:
        if entryPort == "0":
            port0OfS3(source, message, destination)
        elif entryPort == "1":
            port1OfS3(source, message, destination)
        elif entryPort == "2":
            port2OfS3(source, message, destination)
        elif entryPort == "3":
            port3OfS3(source, message, destination)
    else:
        if port != "0":
            port0OfS3(source, message, destination)
        if port != "1":
            port1OfS3(source, message, destination)
        if port != "2":
            port2OfS3(source, message, destination)
        if port != "3":
            port3OfS3(source, message, destination)


def port0OfS4(source, message, destination):
    print(S4port0 + " received message: " + message)


def port1OfS4(source, message, destination):
    S1("0", source, message, destination)


def port2OfS4(source, message, destination):
    print(S4port2 + " received message: " + message)


def port3OfS4(source, message, destination):
    S5("2", source, message, destination)


def S4(port, source, message, destination):
    switchFile = "S4.txt"
    makeEntry(switchFile, source, port)

    entries = [entry.rstrip('\n') for entry in open(switchFile)]

    entryAvailable = False
    entryPort = ""
    for entry in entries:
        entryTokens = entry.split(",")
        entryHost = entryTokens[0]
        entryPort = entryTokens[1]
        if entryHost == destination:
            entryAvailable = True
            break
    if entryAvailable:
        if entryPort == "0":
            port0OfS4(source, message, destination)
        elif entryPort == "1":
            port1OfS4(source, message, destination)
        elif entryPort == "2":
            port2OfS4(source, message, destination)
        elif entryPort == "3":
            port3OfS4(source, message, destination)
    else:
        if port != "0":
            port0OfS4(source, message, destination)
        if port != "1":
            port1OfS4(source, message, destination)
        if port != "2":
            port2OfS4(source, message, destination)
        if port != "3":
            port3OfS4(source, message, destination)


def port0OfS5(source, message, destination):
    print(S5port0 + " received message: " + message)


def port1OfS5(source, message, destination):
    return None


def port2OfS5(source, message, destination):
    S4("3", source, message, destination)


def port3OfS5(source, message, destination):
    print(S5port3 + " received message: " + message)


def S5(port, source, message, destination):
    switchFile = "S5.txt"
    makeEntry(switchFile, source, port)

    entries = [entry.rstrip('\n') for entry in open(switchFile)]

    entryAvailable = False
    entryPort = ""
    for entry in entries:
        entryTokens = entry.split(",")
        entryHost = entryTokens[0]
        entryPort = entryTokens[1]
        if entryHost == destination:
            entryAvailable = True
            break
    if entryAvailable:
        if entryPort == "0":
            port0OfS5(source, message, destination)
        elif entryPort == "1":
            port1OfS5(source, message, destination)
        elif entryPort == "2":
            port2OfS5(source, message, destination)
        elif entryPort == "3":
            port3OfS5(source, message, destination)
    else:
        if port != "0":
            port0OfS5(source, message, destination)
        if port != "1":
            port1OfS5(source, message, destination)
        if port != "2":
            port2OfS5(source, message, destination)
        if port != "3":
            port3OfS5(source, message, destination)


fileName = sys.argv[1]
lines = [line.rstrip('\n') for line in open(fileName)]

numOfSwitches = 5
numOfHosts = 9

for i in range(numOfSwitches):
    fileName = "S" + str(i + 1) + ".txt"
    open(fileName, "a")

for line in lines:

    tokens = line.split(",")
    sourceHost = tokens[0]
    msg = tokens[1]
    destHost = tokens[2]
    print("------------------------------------------------")
    print("Source: " + sourceHost + " | Msg: " + msg + " | Destination: " + destHost)
    print("------------------------------------------------")

    if sourceHost == S1port2:
        S1("2", sourceHost, msg, destHost)
    if sourceHost == S1port1:
        S1("1", sourceHost, msg, destHost)
    elif sourceHost == S4port2:
        S4("2", sourceHost, msg, destHost)
    elif sourceHost == S4port0:
        S4("0", sourceHost, msg, destHost)
    elif sourceHost == S3port1:
        S3("1", sourceHost, msg, destHost)
    elif sourceHost == S3port3:
        S3("3", sourceHost, msg, destHost)
    elif sourceHost == S2port3:
        S2("3", sourceHost, msg, destHost)
    elif sourceHost == S5port0:
        S5("0", sourceHost, msg, destHost)
    elif sourceHost == S5port3:
        S5("3", sourceHost, msg, destHost)
