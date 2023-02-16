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

# TODO: Connect this socket to the relay at relay_port

# TODO: Receive any data relayed from the relay (i.e., any data sent by the client to the relay)

# Print debugging information
print("Data received: ", data)

# Convert received number to binary
data = bin(int(data))

# TODO: Send computed answer back to relay

# Print debugging information
print("Data sent back: ", data)

# TODO: Close any open sockets
