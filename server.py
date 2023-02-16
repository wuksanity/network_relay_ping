import sys
import os
import random
import string
from socket import *

if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a TCP socket for the server
serverSocket = socket(AF_INET, SOCK_STREAM)

# TODO: Connect this socket to the relay at relay_port
serverSocket.connect(("127.0.0.1", relay_port))

# TODO: Receive any data relayed from the relay (i.e., any data sent by the client to the relay)
data = serverSocket.recv(1024)

# Print debugging information
print("Data received: ", data)

# Convert received number to binary
data = bin(int(data))

# TODO: Send computed answer back to relay
serverSocket.send(data.encode())

# Print debugging information
print("Data sent back: ", data)

# TODO: Close any open sockets
serverSocket.close()

