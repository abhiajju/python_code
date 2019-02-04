#!/usr/bin/python2

# receiver's code

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

p=("127.0.0.1",9090)  # recv ip and port

buffer_size = 1024

s.bind(p)  # receiver needs to bind ip and port

print "receiving now \n"

f=open('/root/ab.py','wb')

cnt=0
while True:
	recv = s.recvfrom(buffer_size)
	data = recv[0]
	sock = recv[1]
	while len(data)>0:
		cnt=cnt+1
		f.write(data)
		#print cnt
		s.sendto("got",sock)
		data = s.recvfrom(buffer_size)[0]
	print "done rec"
	print cnt
	break
f.close()
print "connection closed"
s.close()

