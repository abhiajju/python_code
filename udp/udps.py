#!/usr/bin/python2


# senders code

import socket
import commands

ip = "127.0.0.1"  # this is ip of receiver
port = 9090 # recv port

recv_sock = (ip,port)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

i=1
while i<12:
	msg = raw_input("enter your msg")
	s.sendto(msg,recv_sock)  
	i+=1
print " connection ended"
