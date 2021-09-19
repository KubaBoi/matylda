#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
import json
import socket

class Server:
    def __init__(self, animationManager):
        self.animationManager = animationManager

    def serveForever(self):

        self.HOST = ""
        self.PORT = 55573

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                s.bind((self.HOST, self.PORT))
                s.listen(5)
                print("Running...")
                break
            except Exception as e:
                print("Connection is old. Turn of controll script.")
                time.sleep(2)


        conn, addr = s.accept()
        print("Connected by", addr)
        i = 0

        while True:
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    decoded = data.decode("utf-8")
                    request = json.loads(decoded) # array of recieved requests

                    answer = self.animationManager.doRequest(request)

                    conn.sendall(bytes(json.dumps(answer), "utf-8"))

            except Exception as e:
                print("Disconnected by", addr)
                print(str(e))
                print("Waiting...")
                conn, addr = s.accept()
                print("Connected by", addr)


