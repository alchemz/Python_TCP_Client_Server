
import socket

TCP_IP='127.0.0.1'
TCP_PORT=50000
BUFFER_SIZE=1024
MESSAGE="Hello, World!"

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connection to hostname on the port.
s.connect((TCP_IP, TCP_PORT))      
s.send(MESSAGE.encode('utf-8'))
data= s.recv(BUFFER_SIZE)                                                     
s.close()

print("received message:", data)
#print("The time got from the server is %s" % tm.decode('ascii'))












