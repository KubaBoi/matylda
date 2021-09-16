from server import Server
from servoController import ServoController
from animationScripts.animationManager import AnimationManager

controller = ServoController(16)
animationManager = AnimationManager(controller)
server = Server(controller, animationManager)

server.serveForever()
