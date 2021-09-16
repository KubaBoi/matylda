
class AnimationStep:
    def __init__(self, type, speed=None, angle=None, duration=None, otherServo=None):
        self.type = type
        self.speed = speed
        self.angle = angle
        self.duration = duration
        self.otherServo = otherServo
        self.runTime = 0
        