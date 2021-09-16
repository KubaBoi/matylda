#!/usr/bin/env python3
import socket
import json

class Server:
    def __init__(self):
        pass

    def start(self):
        HOST = ""  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        print("Running...")
        conn, addr = s.accept()
        print("Connected by", addr)
        i = 0

        self.down = False

        while True:
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    r = "data"
                    print(r)
                    conn.sendall(bytes(json.dumps(r), "utf-8"))

            except Exception as e:
                print("Disconnected by", addr)
                print(str(i) + ": ")
                print(str(e))
                i += 1

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((HOST, PORT))
                s.listen(5)
                conn, addr = s.accept()
                print("Connected by", addr)
    

touchPad = Server()
touchPad.start()