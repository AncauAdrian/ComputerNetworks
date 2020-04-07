import socket
import time
from datetime import datetime
current_milli_time = lambda: int(round(time.time() * 1000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1234))
s.listen()
cs, address = s.accept()
t = cs.recv(1024).decode()
t.strip('\n\r')
timestamp = time.time_ns() // 1000000

ping = timestamp - int(t)

print(ping)
cs.send((str(ping) + '\n').encode())
cs.close()
