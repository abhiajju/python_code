#!/usr/bin/python2

# receiver's code

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

p=("127.0.0.1",9090)  # recv ip and port

buffer_size = 100

s.bind(p)  # receiver needs to bind ip and port

i=1
while i<12:
	rec_data = s.recvfrom(buffer_size)
	print rec_data[0]

print "connection closed"
s.close()

