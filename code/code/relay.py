import sys
from socket import *

if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections

# Bind the relay's socket to relay_port
relay_listener_socket.bind(("127.0.0.1", relay_port))

# TODO: Put relay_listener_socket in LISTEN mode

# TODO: Accept a connection first from client.py

# TODO: Then, accept a connection from server.py

# TODO: Receive data from client

# TODO: Forward data to server

# Print data that was relayed
print("Data relayed: ", data

# TODO: Recive computed answer from server

# TODO: Forward answer back to client

# Print data that was relayed back
print("Data relayed back: ", data)

# TODO: Close any open sockets
