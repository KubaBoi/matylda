#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
import json
import socket

from servoController import ServoController

class Server:
    def __init__(self, servoController):
        self.controller = servoController

    def start(self):
        HOST = ""
        PORT = 65432

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
                    if not data:
                        break

                    decoded = data.decode("utf-8")
                    moves = json.loads(decoded) # array of recieved moves

                    answer = [] # answer in case of "g"
                    
                    for m in moves:
                        type = m["type"]
                        serv = m["servo"]
                        speed = m["speed"]
                        angle = m["finalAngle"]
                        
                        if (type == "m"): # set move
                            self.controller.serv.setMove(serv, speed, angle)
                        elif (type == "s"): # set angle
                            self.controller.setAngle(serv, angle)
                        elif (type == "g"): # get angle
                            get = {}
                            get["servo"] = serv
                            get["angle"] = self.controller.getAngle(serv)
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

    def doMoves(self):

