#!/usr/bin/python

import commands 

ram = commands.getoutput("free -m").split()[7]
print "\n the ram in the system is ",ram

cpu = commands.getoutput("lscpu").split("\n")[12].split(":")[1]
print "\n the cpu of your system is ",cpu
