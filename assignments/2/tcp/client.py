#!/usr/bin/env python3

from socket import *

serverName = "127.0.0.1"
serverPort = 42069
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input("('date', 'time', or 'exit'): ").upper()

    clientSocket.send(message.encode())

    if message == "EXIT":
        clientSocket.close()
        break

    response = clientSocket.recv(1024).decode()

    print(f"Response: {response}")

