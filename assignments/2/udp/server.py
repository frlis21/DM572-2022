from socket import *
from datetime import datetime

commands = {
    "DATE": lambda: datetime.now().strftime("%A, %B %-d, %Y"),
    "TIME": lambda: datetime.now().strftime("%H:%M"),
}

serverPort = 42069
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server ready!")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decoded = message.decode()
    
    if decoded in commands:
        response = commands[decoded]()
    else:
        response = "ERROR"

    print(f"Processing request: {decoded} -> {response}")
    
    serverSocket.sendto(response.encode(), clientAddress)

