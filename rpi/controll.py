import json
import socket

HOST = "192.168.0.108"  # The server's hostname or IP address
PORT = 55573        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        #m,0,0.01,150|m,1,0.01,150|m,2,0.01,150|g,0|g,1|g,2

        inp = input("type,servo,speed,angle: ")

        request = {}

        if (inp[0] != "a"):
            request["type"] = "m"
            request["requests"] = []
            reqs = inp.split("|")

            for r in reqs:
                req = r.split(",")

                data = {}
                
                data["type"] = req[0]
                data["servo"] = int(req[1])
                if (req[0] != "g"):
                    data["speed"] = float(req[2])
                    data["finalAngle"] = int(req[3])

                request["requests"].append(data)
        else:
            animationPath = inp.split(" ")[1]
            with open(f"./rpi/requests/{animationPath}.json", "r", encoding="utf-8") as f:
                request = json.loads(f.read())

        print(f"Request: {request}")

        s.sendall(bytes(json.dumps(request), "utf-8"))
        recieved = s.recv(1024)
        decoded = recieved.decode("utf-8")
        print(f"Response: {decoded}")