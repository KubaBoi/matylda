import time
from adafruit_servokit import ServoKit
import json
import socket

from servo import Servo

servoCount = 16

pca = ServoKit(channels=servoCount)
servos = []

#init servos
for i in range(servoCount):
    pca.servo[i].set_pulse_width_range(500, 2500)
    
    servos.append(Servo(pca.servo[i], i))
    servos[i].setAngle(1)

print("Initialized")

servos[3].setMove(0.1, 180)

HOST = "192.168.0.104"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"1")
        recieved = s.recv(1024)
        decoded = recieved.decode("utf-8")
        moves = json.loads(decoded)
        
        for m in moves:
            if (m["type"] == "n"): continue
            serv = servos[m["servo"]]
            
            if (m["type"] == "m"):
                serv.setMove(m["speed"], m["finalAngle"])
            elif (m["type"] == "s"):
                serv.setAngle(m["finalAngle"])


        for servo in servos:
            servo.tick()