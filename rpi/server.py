#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
import json
import socket

class Server:
    def __init__(self, servoController):
        self.controller = servoController

    def start(self):
        HOST = ""
        PORT = 55573

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        print("Running...")
        conn, addr = s.accept()
        print("Connected by", addr)
        i = 0

        while True:
            try:
                while True:
                    data = conn.recv(1024)
                    self.controller.tick() # update servos
                    print("tick")
                    if not data:
                        break

                    decoded = data.decode("utf-8")
                    requests = json.loads(decoded) # array of recieved requests

                    answer = [] # answer in case of "g"
                    
                    for m in requests:
                        type = m["type"]
                        index = m["servo"]
                        speed = m["speed"]
                        angle = m["finalAngle"]
                        
                        if (type == "m"): # set move
                            self.controller.setMove(index, speed, angle)
                        elif (type == "s"): # set angle
                            self.controller.setAngle(index, angle)
                        elif (type == "g"): # get angle
                            get = {}
                            get["servo"] = index
                            get["angle"] = self.controller.getAngle(index)
                            answer.append(get)

                    
                    conn.sendall(bytes(json.dumps(answer), "utf-8"))

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

