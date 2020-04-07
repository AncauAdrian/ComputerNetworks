import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1234))

while True:
    print(s.recv(100))
    time.sleep(1)