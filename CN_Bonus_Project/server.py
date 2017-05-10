import socket
from initialSetup import *
import _thread


def interact(client, address):
    nameInBytes = client.recv(1024)
    yInBytes = client.recv(1024)
    name = nameInBytes.decode()
    y = int(yInBytes.decode())
    print("Received from client: ", address, " -- ( " + name + ", " + str(y) + ")")

    t = random.choice([0, 1])
    print("For client: ", address, " -- selected t = " + str(t))
    tInBytes = str.encode((str(t)))
    client.send(tInBytes)

    zInBytes = client.recv(1024)
    z = int(zInBytes.decode())

    passed = False
    zSquareModN = squareNMultiply(z, 2, n)

    if t == 0:
        if zSquareModN == y:
            passed = True
    elif t == 1:
        b = None
        for entry in entries:
            entryName = entry[0]
            entryInformation = entry[1]
            if name == entryName:
                b = entryInformation[0]
                break
        if b is not None:
            if zSquareModN == (b * y) % n:
                passed = True

    if passed:
        print(name + ' - login success')
        msg = 'Welcome ' + name
    else:
        print(name + ' - login failed')
        msg = 'Access Denied'

    msgInBytes = str.encode(msg)
    client.send(msgInBytes)


entries = setup()
n = ((entries[0])[1])[1]

s = socket.socket()
host = ''
port = 8800
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Connection from ', addr)
    _thread.start_new_thread(interact, (c, addr))
