import json
import socket

HOST = "192.168.0.104"  # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        """
        moves[]:
            type[str]:
                m - set move
                s - set angle
                g - get angle
            servo[int]: index
            speed[float]: (0, 1>
            finalAngle[int]: <0, 180>
        """

        inp = input("type,servo,speed,angle: ").split(",")

        requests = []

        data = {}
        data["type"] = inp[0]
        data["servo"] = int(inp[1])
        data["speed"] = float(inp[2])
        data["finalAngle"] = int(inp[3])

        requests.append(data)

        print(requests)

        s.sendall(bytes(json.dumps(requests), "utf-8"))
        recieved = s.recv(1024)
        decoded = recieved.decode("utf-8")
        print(decoded)