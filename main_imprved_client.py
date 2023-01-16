import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "172.16.10.13"                           

port = 9999

# connection to hostname on the port.
clientsocket.connect((host, port))                               


while True:
# Send text input to the server
	message = input("Enter a message to send to the server: ")
	clientsocket.send(message.encode())

# receive data from the server
	response = clientsocket.recv(1024).decode()                                     
	print("Server says: " + response)

clientsocket.close()
