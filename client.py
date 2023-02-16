import sys
import os
import random
import string
from socket import *

if (len(sys.argv) < 3):
  print("Usage: python3 " + sys.argv[0] + " relay_port integer_to_send")
  sys.exit(1)
assert(len(sys.argv) == 3)
relay_port=int(sys.argv[1])

# Read integer
data=sys.argv[2]

# TODO: Create a TCP socket for the client
clientSocket = socket(AF_INET, SOCK_STREAM)

# TODO: Connect client to the relay at the relay_port
clientSocket.connect(("127.0.0.1", relay_port))

# Wait until the server has also connected to the relay
input("Press enter to start transmissions")

# TODO: Send this to the relay for it to forward to the receiver
clientSocket.send(data.encode())

# print debugging information
print("Data sent: " + data)

# TODO: Receive computed answer from relay

data = clientSocket.recv(1024)

# Print received answer
print("Data received: ", data.decode())

# TODO: Close any open sockets
clientSocket.close()

