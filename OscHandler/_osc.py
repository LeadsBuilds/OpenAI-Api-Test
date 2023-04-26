import argparse
from pythonosc import udp_client

class Create:
    def __init__(self):
        ip = "127.0.0.1"
        port = 9000

        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=ip,
            help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=port,
            help="The port the OSC server is listening on")
        args = parser.parse_args()

        self.client = udp_client.SimpleUDPClient(args.ip, args.port)
    
    def sendMessage(self, message: str):
        self.client.send_message('/chatbox/input', str(message))