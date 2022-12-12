import socket

class ARPSC:
    def __init__(self):
        pass
table={
    '192.168.1.1':'1E.4A.4A.11',
    '192.168.2.1':'5E.51.4B.01',
}

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen()
clientsocket,address=s.accept()
print("ConnectionFrom",address,"Has Estableshed")
ip = clientsocket.recv(1024)
ip=ip.decode("utf-8")
mac=table.get(ip,"no entry for given address")
clientsocket.send(mac.encode())

t=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
t.connect(("localhost",1234))
#a = input("ARP OR RARP :")
#if(a=='ARP'):
add=input("Enter IP:")
#elif(a=='RARP'):
#add=input("Enter MAC:")
t.send(add.encode())
mac = t.recv(1024)
mac=mac.decode("utf-8")
print('MAC OF',add,'is:',mac)