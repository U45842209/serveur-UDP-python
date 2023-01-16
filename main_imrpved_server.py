import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "172.16.10.13"                           

port = 9995

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    while True:
        # wait for text input
        message = clientsocket.recv(1024).decode()
        if message:
            print(f"Received: {message} from {str(addr)}")
            
            # process the message here
            response = "Server received: " + message + "\r\n"
            clientsocket.send(response.encode())
        else:
            break
    clientsocket.close()
