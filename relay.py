import sys
from socket import *

if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections
relay_listener_socket = socket(AF_INET, SOCK_STREAM)

# Bind the relay's socket to relay_port
relay_listener_socket.bind(("127.0.0.1", relay_port))

# TODO: Put relay_listener_socket in LISTEN mode
relay_listener_socket.listen(1)

# TODO: Accept a connection first from client.py
connectionSocket, addr = relay_listener_socket.accept()

# TODO: Then, accept a connection from server.py
connectionSocket2, addr2 = relay_listener_socket.accept()

# TODO: Receive data from client
data = connectionSocket.recv(1024)

# TODO: Forward data to server
connectionSocket2.send(data)

# Print data that was relayed
print("Data relayed: ", data)

# TODO: Recive computed answer from server
data = connectionSocket2.recv(1024)

# TODO: Forward answer back to client
connectionSocket.send(data)

# Print data that was relayed back
print("Data relayed back: ", data)

# TODO: Close any open sockets
relay_listener_socket.close()
connectionSocket.close()
connectionSocket2.close()
