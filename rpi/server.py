#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
import json
import socket

class Server:
    def __init__(self, servoController, animationManager):
        self.controller = servoController
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
                time.sleep(1000)


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

                    answer = self.readRequests(request)

                    conn.sendall(bytes(json.dumps(answer), "utf-8"))

            except Exception as e:
                print("Disconnected by", addr)
                print(str(e))
                print("Waiting...")
                conn, addr = s.accept()
                print("Connected by", addr)

    def readRequests(self, request):
        answer = [] # answer in case of "g"
                    
        type = request["type"] # a/m

        if (type == "m"):
            requests = request["requests"] # list of moves
            
            for r in requests:
                req_type = r["type"]
                index = r["servo"]
                speed = r["speed"]
                angle = r["finalAngle"]
                
                if (req_type == "m"): # set move
                    self.controller.setMove(index, speed, angle)
                elif (req_type == "s"): # set angle
                    self.controller.setAngle(index, angle)
                elif (req_type == "g"): # get angle
                    get = {}
                    get["servo"] = index
                    get["angle"] = self.controller.getAngle(index)
                    answer.append(get)

            self.controller.tick()

        elif (type == "a"):
            print("ANIMATION")
            self.animationManager.createAnimation(request)
            self.animationManager.runAnimation()

        return answer

