from netmiko import ConnectHandler

#First create the device object using a dictionary
CSR = {
    "device_type": "cisco_ios",
    #"device_type": "cisco_ioxs",
    #"ip": "sandbox-iosxe-recomm-1.cisco.com",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    #"port": 80
}

# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)

# Then send the command and print the output
#output = net_connect.send_command('show ip int brief')

#output_clock=net_connect.send_command('show clock')

#output_route=net_connect.send_command('show ip ro')

output_runconfig=net_connect.send_command('show run')
print (output_runconfig)

# Finally close the connection
net_connect.disconnect()

