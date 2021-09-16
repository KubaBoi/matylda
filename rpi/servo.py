#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Servo:
    def __init__(self, servo, pin):
        self.servo = servo
        self.pin = pin

    #speed (0, 1>
    #finalAngle <0, 180>
    def setMove(self, speed, finalAngle):
        self.active = True
        
        self.oldAngle = self.getAngle()
        self.finalAngle = finalAngle
        
        self.time = 0 # move time
        self.speed = speed

    def tick(self):
        if (self.isActive()):
            if (self.getAngle() == self.finalAngle):
                self.printServoInfo()
                print("STOP")
                self.active = False

            else:
                self.setAngle(self.lerp())
                self.time += self.speed

    def lerp(self):
        return round((1 - self.time) * self.oldAngle + self.time * self.finalAngle)

    def isActive(self):
        return self.active

    def getAngle(self):
        return round(self.servo.angle)

    def addAngle(self, value):
        self.printServoInfo(f"Adding: {value}")
        val = self.getAngle() + value
        self.servo.angle = val

    def setAngle(self, value):
        self.printServoInfo(f"Setting: {value}")
        self.servo.angle = value

    def printServoInfo(self, comment=""):
        print(f"Servo: {self.pin} angle: {self.getAngle} {comment}") 