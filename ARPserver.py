#first of all import the socket module
import socket

s=socket.socket()
print("Socket created successfully")

port=40674

s.bind(('',port))
print("socket bindedto %s" %(port))

s.listen(5)
print("socket is listening")

while True:

	c, addr=s.accept()
	print('Got connection from',addr)
	
	c.send(b'Thank you for connecting')
	
	c.close()