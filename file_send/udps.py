#!/usr/bin/python2


# senders code

import socket
import commands

ip = "127.0.0.1"  # this is ip of receiver
port = 9090 # recv port

recv_sock = (ip,port)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


buffer_size = 1024
cnt =0

while True:
	f=open('/root/index','rb')
	l=f.read(buffer_size)
	while (l):
		s.sendto(l,recv_sock)  
		cnt = cnt+1
		#print cnt
		s.recvfrom(buffer_size)
		l=f.read(buffer_size)
	f.close()
	s.sendto("",recv_sock)
	break
print cnt
print " connection ended"

