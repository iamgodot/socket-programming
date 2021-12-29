#!/usr/local/bin/python3

import socket

ADDR = "127.0.0.1"
PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# s.bind((ADDR, PORT))
# s.listen()
with socket.create_server((ADDR, PORT)) as s:  # Convenient function
    conn, addr = s.accept()  # accept blocks
    print("Connected by ", addr)
    while True:
        data = conn.recv(3)
        print(data)
        if not data:
            conn.close()  # Better close here explicitly
            break
        conn.sendall(data)
