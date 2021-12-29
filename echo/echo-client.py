#!/usr/local/bin/python3

import socket

ADDR = "127.0.0.1"
PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# s.connect((ADDR, PORT))  # blocking calls, as well as send and recv
with socket.create_connection((ADDR, PORT)) as s:  # Convenient function
    s.sendall(b"Hello world!")
    # 这里的 recv 不一定会返回全部的数据，如果只返回了部分
    # 那么 socket close 之后，就会造成数据丢失（缓冲区），
    # 此时 client 会发送 RST 给对方
    # s.settimeout(5)
    length = 0
    while data := s.recv(1024):
        print("Received: ", data)
        length += len(data)
        if length >= 12:
            break
