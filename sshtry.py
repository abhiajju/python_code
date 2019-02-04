#!/usr/bin/python2

import os
import commands

msg = "AllowUsers harry@192.168.43.89"

ip = ["192.168.43.77","192.168.43.236"]
passwd = ["5390","qwe"]
fil = "/etc/ssh/sshd_conf"

content =  commands.getoutput("cat /etc/ssh/sshd_config")

'''
length = len(ip)


for i in range(length):
	ssh = "sshpass -p "+passwd[i]+" ssh root@"+ip[i]
	command = " 'echo '"+content+"' > '"+fil 
	commands.getstatusoutput(ssh+command)
	print "done "
'''
