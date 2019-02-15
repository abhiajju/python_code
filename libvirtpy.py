#!/usr/bin/python2

import commands,libvirt,json

print " Listing all of your vms"

conn=libvirt.open("qemu:///system")

ids = conn.listDomainsID()
print ids

names = []
state = []
max_memory = []
cpu_count = []
for i in ids:
        lookup=conn.lookupByID(i)
        info=lookup.info()
	nm=lookup.name()
	names.append(nm)
        max_memory.append(info[1])
	cpu_count.append(info[3])
	if(info[0]==1):
		state.append('running')
        elif info[0]==3:
        	state.append('paused')
	else:
		state.append('stopped')
               

#print names , state , max_memory , cpu_count

print "ID\t\tNAME\t\tSTATE"
print "-------------------------------------------------------------"
l = len(ids)
for i in range(0,l):
	print ids[i],'\t\t',names[i],'\t',state[i]


while True:
	choice = int(raw_input('Select an id to know about its network details'))
	try:
		choice_id = ids.index(choice)
		break
	except:
		print '\nValue '+str(choice)+' could not be found!! Try Again\n'


dom_name = names[choice_id]

net_details = commands.getstatusoutput('virsh domifaddr '+dom_name)
print '\n'
print ' Network details for '+dom_name+' :'
if net_details[0]==0:
	print net_details[1]
else:
	print 'Oops!! An error has occured'
	print net_details[1]


#ip address of vm
#print net_details[1].split('\n')[2].split(' ')[-1]


