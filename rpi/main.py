import time
from adafruit_servokit import ServoKit

from servo import Servo

servoCount = 16

pca = ServoKit(channels=servoCount)
servos = []

#init servos
for i in range(servoCount):
    pca.servo[i].set_pulse_width_range(500, 2500)
    
    servos.append(Servo(pca.servo[i], i))
    servos[i].setAngle(0)

print("Initialized")

servos[0].setMove(0.1, 180)

#run
while True:
    for servo in servos:
        servo.tick()

    time.sleep(0.01)