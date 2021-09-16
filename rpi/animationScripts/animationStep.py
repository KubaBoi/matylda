
class AnimationStep:
    def __init__(self, type, speed=0, angle=0, duration=0, otherServo=-1):
        self.type = type
        self.speed = speed
        self.angle = angle
        self.duration = duration
        self.otherServo = otherServo
        self.runTime = 0
        