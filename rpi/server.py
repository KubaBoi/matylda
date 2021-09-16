#!/usr/bin/env python3
import socket
import json

class Server:
    def __init__(self):
        pass

    def start(self):
        HOST = ""
        PORT = 65432

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        print("Running...")
        conn, addr = s.accept()
        print("Connected by", addr)
        i = 0

        while True:
            try:
                i = 0
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    """
                    moves[]:
                        type[str]:
                            n - nothing 
                            m - set move
                            s - set angle
                            g - get angle
                        servo[int]: index
                        speed[float]: (0, 1>
                        finalAngle[int]: <0, 180>
                    """

                    moves = []

                    answer = {}
                    answer["type"] = "m"
                    answer["servo"] = 0
                    answer["speed"] = 0.1
                    answer["finalAngle"] = 180

                    moves.append(answer)

                    print(moves)
                    conn.sendall(bytes(json.dumps(moves), "utf-8"))

            except Exception as e:
                print("Disconnected by", addr)
                print(str(i) + ": ")
                print(str(e))
                i += 1

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((HOST, PORT))
                s.listen(5)
                conn, addr = s.accept()
                print("Connected by", addr)
    

touchPad = Server()
touchPad.start()