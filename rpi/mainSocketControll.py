import time
from adafruit_servokit import ServoKit
import json
from tkinter.constants import NONE
import pyautogui
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

HOST = "192.168.0.107"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"1")
        recieved = s.recv(1024)
        decoded = recieved.decode("utf-8")
        data = json.load(decoded)
        print(data)

        for servo in servos:
            servo.tick()