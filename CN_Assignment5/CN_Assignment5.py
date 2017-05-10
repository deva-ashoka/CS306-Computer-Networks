# CN Assignment 5
# Name: Deva Surya Vivek Madala
import sys
import binascii


class Host:
    def __init__(self, ip, sm, sn):
        self.ipAddress = ip
        self.subnetMask = sm
        self.subnetNumber = sn


class Packet:
    def __init__(self, sourceIP, destinationIP, sequenceNumber, flag, offset, msg):
        self.sourceIP = sourceIP
        self.destinationIP = destinationIP
        self.sequenceNumber = sequenceNumber
        self.flag = flag
        self.offset = offset
        self.msg = msg


def sendPacketsToHost(hostNumber, packets):
    f = open("output.txt", 'a')
    f.write("Packets Received by " + hostNumber + "!\n")
    finalMessageInBits = ""
    seqNum = packets[0].sequenceNumber
    for packet in packets:
        if packet.sequenceNumber == seqNum:
            finalMessageInBits += packet.msg
        if packet.flag == 0:
            break
    finalMessageInText = textFromBits(finalMessageInBits)
    f.write("Message received: " + finalMessageInText + '\n')
    f.close()


def Router(router, destinationSubnetNumber, packets):
    f = open("output.txt", 'a')
    f.write("Packets Received by " + router + " :\n")
    i = 0
    for packet in packets:
        f.write("     Packet " + str(i) + " :\n")
        i += 1
        f.write("         Source IP: " + packet.sourceIP + '\n')
        f.write("         Destination IP: " + packet.destinationIP + '\n')
        f.write("         Sequence Number: " + str(packet.sequenceNumber) + '\n')
        f.write("         Flag: " + str(packet.flag) + '\n')
        f.write("         Offset: " + str(int(packet.offset / 8)) + '\n')
        f.write("         Message: " + packet.msg + '\n')
    f.write("------------------------------------------------------------------------\n")
    f.close()

    if router == destinationSubnetNumber:
        packet = packets[0]
        if router == "S1":
            if packet.destinationIP == H1.ipAddress:
                sendPacketsToHost("H1", packets)
            elif packet.destinationIP == H2.ipAddress:
                sendPacketsToHost("H2", packets)
            elif packet.destinationIP == H11.ipAddress:
                sendPacketsToHost("H11", packets)
        elif router == "S2":
            if packet.destinationIP == H7.ipAddress:
                sendPacketsToHost("H7", packets)
        elif router == "S3":
            if packet.destinationIP == H5.ipAddress:
                sendPacketsToHost("H5", packets)
            elif packet.destinationIP == H6.ipAddress:
                sendPacketsToHost("H6", packets)
            elif packet.destinationIP == H10.ipAddress:
                sendPacketsToHost("H10", packets)
        elif router == "S4":
            if packet.destinationIP == H3.ipAddress:
                sendPacketsToHost("H3", packets)
            elif packet.destinationIP == H4.ipAddress:
                sendPacketsToHost("H4", packets)
        elif router == "S5":
            if packet.destinationIP == H8.ipAddress:
                sendPacketsToHost("H8", packets)
            elif packet.destinationIP == H9.ipAddress:
                sendPacketsToHost("H9", packets)
            elif packet.destinationIP == H12.ipAddress:
                sendPacketsToHost("H12", packets)
    else:
        routerFile = router + ".txt"
        entries = [entry.rstrip('\n') for entry in open(routerFile)]
        nextRouter = None
        for entry in entries:
            entryTokens = entry.split(",")
            if entryTokens[0] == destinationSubnetNumber:
                nextRouter = entryTokens[1]
                break
        packetsForNextRouter = []
        for packet in packets:
            nextPackets = modifyPacketsForNextRouter(nextRouter, packet)
            for p in nextPackets:
                packetsForNextRouter.append(p)

        Router(nextRouter, destinationSubnetNumber, packetsForNextRouter)


def modifyPacketsForNextRouter(router, packet):
    packets = []
    MTU = None
    if router == "S1":
        MTU = 1500 * 8
    if router == "S2":
        MTU = 1000 * 8
    if router == "S3":
        MTU = 500 * 8
    if router == "S4":
        MTU = 500 * 8
    if router == "S5":
        MTU = 2000 * 8

    if len(packet.msg) <= MTU:
        packets.append(packet)

    else:

        numOfPacketsRequired = 1
        messageLength = len(packet.msg)
        while messageLength > MTU * numOfPacketsRequired:
            numOfPacketsRequired += 1

        for i in range(numOfPacketsRequired):
            flag = 1
            startIndex = i * MTU
            if i != numOfPacketsRequired - 1:
                endIndex = startIndex + MTU
            else:
                endIndex = messageLength
                if packet.flag == 0:
                    flag = 0
            m = packet.msg[startIndex:endIndex]
            p = Packet(sourceHost.ipAddress, destinationIpAddress, packet.sequenceNumber, flag,
                       packet.offset + startIndex, m)
            packets.append(p)

    return packets


def createPacketsForDefaultRouter(router, sourceHost, message, destinationHost):
    packets = []
    MTU = None
    if router == "S1":
        MTU = 1500 * 8
    if router == "S2":
        MTU = 1000 * 8
    if router == "S3":
        MTU = 500 * 8
    if router == "S4":
        MTU = 500 * 8
    if router == "S5":
        MTU = 2000 * 8

    messageInBits = textToBits(message)

    global sequenceNumber
    global hosts

    idx = hosts.index(sourceHost)
    seqNum = sequenceNumber[idx]
    sequenceNumber[idx] += 1

    if len(messageInBits) <= MTU:

        p = Packet(sourceHost.ipAddress, destinationHost.ipAddress, seqNum, 0, 0, messageInBits)
        packets.append(p)

    else:

        numOfPacketsRequired = 1
        messageLength = len(messageInBits)
        while messageLength > MTU * numOfPacketsRequired:
            numOfPacketsRequired += 1

        for i in range(numOfPacketsRequired):
            flag = 1
            startIndex = i * MTU
            if i != numOfPacketsRequired - 1:
                endIndex = startIndex + MTU
            else:
                endIndex = messageLength
                flag = 0
            m = messageInBits[startIndex:endIndex]
            p = Packet(sourceHost.ipAddress, destinationIpAddress, seqNum, flag, startIndex, m)
            packets.append(p)

    return packets


def textToBits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def textFromBits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


numOfRouters = 5
numOfHosts = 9

# 255.255.255.0 (Subnet mask) means first 24 bits of ip are fixed for that particular subnet

# For S1, ip -> 10.0.1.x
H1 = Host("10.0.1.1", "255.255.255.0", "S1")
H2 = Host("10.0.1.2", "255.255.255.0", "S1")
H11 = Host("10.0.1.11", "255.255.255.0", "S1")

# For S4, ip -> 10.0.4.x
H3 = Host("10.0.4.3", "255.255.255.0", "S4")
H4 = Host("10.0.4.4", "255.255.255.0", "S4")

# For S3, ip -> 10.0.3.x
H5 = Host("10.0.3.5", "255.255.255.0", "S3")
H6 = Host("10.0.3.6", "255.255.255.0", "S3")
H10 = Host("10.0.3.10", "255.255.255.0", "S3")

# For S2, ip -> 10.0.2.x
H7 = Host("10.0.2.7", "255.255.255.0", "S2")

# For S5, ip -> 10.0.5.x
H8 = Host("10.0.5.8", "255.255.255.0", "S5")
H9 = Host("10.0.5.9", "255.255.255.0", "S5")
H12 = Host("10.0.5.12", "255.255.255.0", "S5")

hosts = [H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12]
sequenceNumber = [0] * 12

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

f = open("output.txt", 'w')
f.close()

sourceIpAddress = lines[0]
destinationIpAddress = lines[1]
message = lines[2]

sourceHost = None
destinationHost = None

for host in hosts:
    if host.ipAddress == sourceIpAddress:
        sourceHost = host
        break

for host in hosts:
    if host.ipAddress == destinationIpAddress:
        destinationHost = host
        break

destinationSubnetNumber = destinationHost.subnetNumber
defaultRouter = sourceHost.subnetNumber

packets = createPacketsForDefaultRouter(defaultRouter, sourceHost, message, destinationHost)

Router(defaultRouter, destinationSubnetNumber, packets)
