#!/usr/bin/python2

import commands

ab="abcdbcddefabcdeabcd"
substr="bcd"
l=len(ab)

i=0

while i<l:
	sub=ab[i:]
	index=sub.find(substr)
	if index==-1:
		break
	i=i+index+1
	print i+len(substr)-2
