from adafruit_servokit import ServoKit

from servo import Servo

class ServoController:
    def __init__(self, servoCount):
        pca = ServoKit(channels=servoCount)
        self.servos = []

        for i in range(servoCount):
            pca.servo[i].set_pulse_width_range(500, 2500)
            
            self.servos.append(Servo(pca.servo[i], i))
            self.testServo(i)

        print("Initialized")
        
    def tick(self):
        while not self.allUnactive():
            for servo in self.servos:
                servo.tick()

    def testServo(self, index):
        ang = self.getAngle(index)
        if (ang != None):
            print(f"Servo {index} is OK")
        else:
            print(f"Servo {index} is NOT OK")


    def setMove(self, servoIndex, speed, finalAngle):
        self.servos[servoIndex].setMove(speed, finalAngle)

    def setAngle(self, servoIndex, angle):
        self.servos[servoIndex].setAngle(angle)

    def getAngle(self, servoIndex):
        return self.servos[servoIndex].getAngle()

    def allUnactive(self):
        for servo in self.servos:
            if (servo.isActive()):
                return False
        return True

    def getServo(self, servoIndex):
        return self.servos[servoIndex]