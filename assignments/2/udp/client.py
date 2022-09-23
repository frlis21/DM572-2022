from socket import *

serverName = "127.0.0.1"
serverPort = 42069
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("('date', 'time', or 'exit'): ").upper()

    if message == "EXIT":
        clientSocket.close()
        break

    clientSocket.sendto(message.encode(), (serverName, serverPort))
    response, serverAddress = clientSocket.recvfrom(2048)

    print(f"Response: {response.decode()}")

