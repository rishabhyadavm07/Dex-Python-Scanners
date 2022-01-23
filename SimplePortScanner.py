#!/usr/bin/python

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#the above program line makes a socked object for IPv4 - socket.AF_INET, socket.SOCK_STREAM - if for using TCP protocol

# now we will be adding raw inputs functionality to this program
IP = input("Enter the IP you want to scan: ")
pt= input("Enter the port you want to run the scan on: ")

# now we will be declaring some variables to feed to the program

Host = IP
Port = int(pt)

# now we will be making a function that will try to connect to a port number present in the port variable

def portscanner(Port):
    if sock.connect_ex((Host, Port)):
        print("Port %d is closed !"%(Port))
    else:
        print("Port %d is open !" %(Port))


# now will be calling the function that we just made
portscanner(Port)

