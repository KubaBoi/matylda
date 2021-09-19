import json

from animationScripts.animation import Animation
from animationScripts.animationStep import AnimationStep

class AnimationManager:
    def __init__(self, servoController):
        self.controller = servoController

    def doRequest(self, data):
        answer = []

        type = data["type"] # a/m

        if (type == "m"):
            requests = data["requests"] # list of moves
            
            for r in requests:
                req_type = r["type"]
                index = r["servo"]

                if (req_type == "g"): # get angle
                    get = {}
                    get["servo"] = index
                    get["angle"] = self.controller.getAngle(index)
                    answer.append(get)
                
                else:
                    speed = r["speed"]
                    angle = r["finalAngle"]
                    
                    if (req_type == "m"): # set move
                        self.controller.setMove(index, speed, angle)
                    elif (req_type == "s"): # set angle
                        self.controller.setAngle(index, angle)

            self.controller.tick()

        elif (type == "a"):
            self.animationManager.createAnimation(data)
            self.animationManager.runAnimation()

        return answer

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
