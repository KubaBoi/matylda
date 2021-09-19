from colors import bcolors as bc

class Animation:
    def __init__(self, servo):
        self.servo = servo
        self.step = 0
        self.steps = []
        self.done = False
        self.oldStep = None

    def addStep(self, step):
        self.steps.append(step)

    def doStep(self):
        if (self.done): return # animation is all done

        step = self.steps[self.step]
        step.runTime += 1

        if (step.type == "m"):
            stepDone = self.doMove(step)
        elif (step.type == "w"):
            stepDone = self.doWait(step)
        elif (step.type == "wu"):
            stepDone = self.doWaitUntil(step)

        self.oldStep = step

        if (stepDone):
            self.step += 1
            if (self.step >= len(self.steps)):
                self.done = True

    def doMove(self, step):
        if (self.steps[self.step] != self.oldStep):
            self.servo.setMove(step.speed, step.angle)

        self.servo.tick()

        if (self.servo.isActive()):
            return False
        return True

    def doWait(self, step):
        self.servo.printServoInfo(f"{bc.WARNING}Waiting for {step.runTime}/{step.duration} ticks{bc.ENDC}")

        if (step.runTime < step.duration):
            return False
        return True

    def doWaitUntil(self, step):
        self.servo.printServoInfo(f"{bc.WARNING}Waiting for {step.otherServo.servoInfo()} to have angle: {step.angle}{bc.ENDC}")

        if (step.angle != step.otherServo.getAngle()):
            return False
        return True
