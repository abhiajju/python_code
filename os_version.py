#!/usr/bin/python

import commands
import ram_cpu as rc
os_version = commands.getoutput("cat /etc/redhat-release")
print "Your os version is ",os_version


print "i am prinitng ",rc.ram
print "done showing everything"

