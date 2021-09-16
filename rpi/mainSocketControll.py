from server import Server
from servoController import ServoController

controller = ServoController(16)
server = Server(controller)

server.serveForever()
