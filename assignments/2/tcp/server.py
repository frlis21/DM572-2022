#!/usr/bin/env python3

from socket import *
from datetime import datetime

commands = {
    "DATE": lambda: datetime.now().strftime("%A, %B %-d, %Y"),
    "TIME": lambda: datetime.now().strftime("%H:%M"),
}

serverPort = 42069
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server ready!")

while True:
    connectionSocket, addr = serverSocket.accept()

    while True:
        message = connectionSocket.recv(1024).decode()
        
        if message in commands:
            response = commands[message]()
        elif message == "EXIT":
            break
        else:
            response = "ERROR"

        print(f"Processing request: {message} -> {response}")
    
        connectionSocket.send(response.encode())

    connectionSocket.close()

