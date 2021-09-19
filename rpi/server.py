#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
import json
import socket
from colors import bcolors as bc

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
                print(f"{bc.OKCYAN}Running...{bc.ENDC}")
                break
            except Exception as e:
                print(f"{bc.WARNING}Connection is old. Turn of controll script.{bc.ENDC}")
                time.sleep(2)


        conn, addr = s.accept()
        print(f"{bc.HEADER}Connected by {addr}{bc.ENDC}")

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
                print(f"{bc.WARNING}Disconnected by {addr}{bc.ENDC}")
                print(f"{bc.FAIL}{str(e)}{bc.ENDC}")
                print(f"{bc.OKCYAN}Waiting...{bc.ENDC}")
                conn, addr = s.accept()
                print(f"{bc.OKCYAN}Connected by {addr}{bc.OKCYAN}")


