import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(0, 1000):
    s.sendto(b'nice', ("172.30.3.3", 9999))
    time.sleep(1)
