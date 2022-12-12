import pinging
import sys



class Main:
    def __init__(self):
    
        self.PI=pinging.Pinging()
        
    def DBImplementation(self):
        import DBImplementation
        
    def ARPS(self):
        import ARPS
        
    def ARPC(self):
        import ARPC
        
    def Bandwidth(self):
        import bandwidth
        
def Systemexiting():
    print("System exiting!")
    
def Printerror():
    print("Invalid choice entered!")
    
m=Main()

def run():
    menu = {
        
        1:m.DBImplementation,
        2:m.ARPS,
        3:m.ARPC,
        4:m.Bandwidth,
        5:Systemexiting
    }
    while True:
        print("\n 1:DBImplementation,\n 2:ARP server,\n 3:ARP client,\n 4:Bandwidth,\n 5:System exiting,\n Enter your choice?",end='')
        try:
            choice = int(input())
        except ValueError:
            print("Please enter the valid input!")
        menu.get(choice,Printerror)()
run()

