import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "172.16.10.13"

port = 9999

# connection to hostname on the port.
clientsocket.connect((host, port))                               

# receive data from the server
msg = clientsocket.recv(1024)                                     

clientsocket.close()
print (msg.decode('ascii'))
