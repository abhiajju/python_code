import socket
import thread
     
def send():
        rec_ip1="192.168.43.237"
        rec_port=9090
	rec_ip2="192.168.43.77"
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        while  True:
    		data=raw_input()
    		s.sendto(data,(rec_ip1,rec_port))
    		s.sendto(data,(rec_ip2,rec_port))
    	#print  s.recvfrom(11)
     
     
def recv():
        rec_ip="192.168.43.233"
        rec_port=9090
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((rec_ip,rec_port)) 
        while True:
    		rec_data=s.recvfrom(100)
    		print rec_data[1][0]," :   ",rec_data[0]
     
     
thread.start_new_thread(send,())
thread.start_new_thread(recv,())
while True:
        pass
