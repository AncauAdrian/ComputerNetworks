import socket
import time
import pickle
import json
from threading import Thread


def handler(con, i):
    for j in range(5):
        rec = con.recv(1024).decode()
        rec.strip('\n\r')
        timestamp = time.time_ns() // 1000000
        ping = timestamp - int(rec)

        con.send((str(ping) + '\n').encode())


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 1234))
    s.listen()

    i = 0

    while True:
        i += 1

        con, addr = s.accept()

        t = Thread(target=handler, args=(con, i,))
        print("New connection from: " + str(addr) + "\nID: " + str(i) + '\n')
        t.start()


main()
