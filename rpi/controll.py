import time
from adafruit_servokit import ServoKit
import json
import socket

HOST = "192.168.0.108"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"1")
        recieved = s.recv(1024)
        decoded = recieved.decode("utf-8")
        
        """
        moves[]:
            type[str]:
                m - set move
                s - set angle
                g - get angle
            servo[int]: index
            speed[float]: (0, 1>
            finalAngle[int]: <0, 180>
        """

        moves = []

        data = {}
        data["type"] = "m"
        data["servo"] = 0
        data["speed"] = 0.1
        data["finalAngle"] = 180

        moves.append(data)

        print(moves)


        for servo in servos:
            servo.tick()