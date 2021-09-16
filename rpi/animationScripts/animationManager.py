import json

from animationScripts.animation import Animation
from animationScripts.animationStep import AnimationStep

class AnimationManager:
    def __init__(self, servoController):
        self.controller = servoController

    def createAnimation(self, data):
        self.animations = []

        for servo in data["servos"]:
            animation = Animation(self.controller.getServo(servo["servo"]))

            for move in servo["moves"]:

                if (move["type"] == "m"):
                    animation.addStep(AnimationStep(
                        type="m",
                        speed=move["speed"],
                        angle=move["finalAngle"]
                    ))
                elif (move["type"] == "w"):
                    animation.addStep(AnimationStep(
                        type="w",
                        duration=move["duration"]
                    ))
                elif (move["type"] == "wu"):
                    animation.addStep(AnimationStep(
                        type="wu",
                        otherServo=self.controller.getServo(move["servo"]),
                        angle=move["angle"]
                    ))

            self.animations.append(animation)

    def runAnimation(self):
        while True:
            cont = False
            for animation in self.animations:
                animation.doStep()
                if (not animation.done):
                    cont = True

            if (not cont): break
