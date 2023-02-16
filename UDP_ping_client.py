from socket import *
import time
import decimal

# creating UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# setting reply wait time to 1 second
clientSocket.settimeout(1)

# sending 10 pings
for i in range(1, 11):

    # sending ping, formatting ping
    send_time = time.time()
    fmt = time.strftime("%H:%M:%S")
    clientSocket.sendto(f"PING {i} {fmt}".encode(), ("127.0.0.1", 12000))

    try:
        decimal.getcontext().prec = 25
        receive_time = time.time()
        message, addr = clientSocket.recvfrom(2048)
        print(f"<{message}>, RTT({i}) = {decimal.Decimal(receive_time - send_time)} seconds")

    except timeout:
        print("Request timed out")


