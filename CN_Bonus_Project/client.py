import socket
from initialSetup import *

s = socket.socket()
host = ''
port = 8800

s.connect((host, port))

name = input("Enter name: ")
x = int(input("Enter a random number x: "))

lines = [line.rstrip('\n') for line in open('n.txt')]
n = int(lines[0])

y = squareNMultiply(x, 2, n)

nameInBytes = str.encode(name)
yInBytes = str.encode(str(y))

s.send(nameInBytes)
s.send(yInBytes)

tInBytes = s.recv(1024)
t = int(tInBytes.decode())

print("Received t = " + str(t))

z = int(input("Enter z: "))

zInBytes = str.encode(str(z))
s.send(zInBytes)

msgInBytes = s.recv(1024)
msg = msgInBytes.decode()

print(msg)
s.close()
