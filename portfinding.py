import pinging
import socket
import subprocess
import sys

from datetime import datetime

class Portfinding:
    def __init__(self):
        pass
        
subprocess.call('clear+', shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("_"*60)
print("Please wait, scanning remote host", remoteServerIP)
print("_"*60)

t1 = datetime.now()

try:
    for port in range(1,200):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:      open".format(port))
            sock.close()
            
except KeyboardInterrupt:
    print("Youbpressed Ctrl+C")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
    
except socket.error:
    print("Couldn't connect be server")
    sys.exit()
t2 = datetime.now()
total = t2-t1 
print("Scanning completed in ",total) 