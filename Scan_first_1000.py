#!/usr/bin/python

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


IP = input("Enter the IP you want to scan: ")



Host = IP
Port = 0


def portscanner(Port):
    if sock.connect_ex((Host, Port)):
        print("Port %d is closed !"%(Port))
    else:
        print("Port %d is open !" %(Port))

print("NOTE: This might take some time. Grab your coffee !")

for i in range(1,1001):
    Port=i
    portscanner(Port)



