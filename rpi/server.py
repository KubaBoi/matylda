#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
import json
import socket
from _thread import *
import threading

class Server:
    def __init__(self, servoController):
        self.controller = servoController
        self.startServer()

    def start(self):
        while True:
            self.controller.tick() # update servos

            start_new_thread(self.serverThread, (self.s,))

    def startServer(self):
        self.print_lock = threading.Lock()

        self.HOST = ""
        self.PORT = 55573

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(5)
        print("Running...")

    def serverThread(self, s):
        try:
            conn, addr = s.accept()
            self.print_lock.acquire()
            print("Connected by", addr)
            i = 0
            while True:
                data = conn.recv(1024)
                if not data:
                    self.print_lock.release()
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
            conn.close()

        except Exception as e:
            print("Disconnected by", addr)
            print(str(i) + ": ")
            print(str(e))
            i += 1

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(5)
            conn, addr = s.accept()
            print("Connected by", addr)

