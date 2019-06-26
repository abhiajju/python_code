#!/usr/bin/python2
import commands

f=open('/etc/hosts','a')
for i in range(0,4):
	msg='nodes[i].example.com'
	f.write(msg)
f.close()
