#!/usr/bin/python2

import os, commands,time,libvirt

nodes = ['master','node1','node2']
ram = [2500,1000,1000]
cpu = [2,1,1]
path = '/var/lib/libvirt/images'
ip=commands.getoutput('myipg')

def fetch_vm_ip():
	conn=libvirt.open("qemu:///system")
	ids = conn.listDomainsID()
	l = len(ids)
	names = []
	for i in ids:
		lookup=conn.lookupByID(i)
		info=lookup.info()
		nm=lookup.name()
		names.append(nm)
	names.sort()
	return names

def get_ip(vm_name):
        ip = commands.getstatusoutput('virsh domifaddr '+vm_name)
        ip = ip[1].split('\n')[2].split(' ')[-1].split('/')[0]
	return ip



# destroying existing vms of cluster
for i in nodes:
	commands.getoutput('virsh destroy '+i)
	commands.getoutput('virsh undefine '+i)
	print 'destroyed vm of '+i

# removing snapshots
for i in nodes:
	commands.getoutput('rm -rvf '+path+'/'+i+'.qcow2')
	print 'snapshot removed for '+i

#creating snapshots 
for i in nodes:
	commands.getoutput('qemu-img create -f qcow2 -b '+path+'/kube1.qcow2 '+path+'/'+i+'.qcow2')
	print 'snapshots created for '+i


#booting the vms
for i in range(0,len(nodes)):
	commands.getoutput('virt-install --name '+nodes[i]+' --ram '+str(ram[i])+' --vcpu '+str(cpu[i])+' --noautoconsole --disk path='+path+'/'+nodes[i]+'.qcow2 --import --os-type linux --os-variant=rhel7')
	time.sleep(8)
	print 'booting done in node:',i


#creating a yum repository for kubernetes using file handling 
msg = '[ku] \nbaseurl=ftp://'+ip+'/pub/rhel7rpm \ngpgcheck=0\n'
f=open('/etc/yum.repos.d/kube.repo','w')
f.write(msg)
f.close()


#installing packages
commands.getoutput('yum install epel-release arp-scan sshpass -y')



#making yum of kubernetes for clusters
msg = '[a] \nbaseurl=ftp://'+ip+'/pub/rhel75 \ngpgcheck=0\n'
f=open('/etc/yum.repos.d/main.repo','a+')
f.write(msg)
f.close()

msg = '[b] \nbaseurl=ftp://'+ip+'/pub/adhoc/kubernetes \ngpgcheck=0\n'
f=open('/etc/yum.repos.d/main.repo','a+')
f.write(msg)
f.close()


# code tested before this point ---------------------------------------

#fetching ips of the nodes
cluster_ip=[]
names=fetch_vm_ip()
for i in nodes:
	idx = names.index(i)
	cluster_ip.append(get_ip(names[idx]))


for i in range(0,len(cluster_ip)):
	commands.getoutput('sshpass -p redhat  ssh  -o  StrictHostKeyChecking=no '+cluster_ip[i]+' echo " '+cluster_ip[i]+' '+nodes[i]+'.example.com " >> /etc/hosts')

f=open('/etc/hosts','a')
for i in range(0,len(cluster_ip)):
	msg=cluster_ip[i]+'  '+nodes[i]+'  '+nodes[i]+'.example.com\n'
	f.write(msg)
f.close()
	



for i in nodes:
	commands.getoutput('sshpass -p redhat scp -o StrictHostKeyChecking=no /etc/yum.repos.d/main.repo root@'+i+':/etc/yum.repos.d/')

#software installation in clusters
for i in range(0,len(cluster_ip)):
	commands.getoutput('sshpass -p redhat ssh root@'+cluster_ip[i]+' yum install vim bash-completion net-tools kubectl kubeadm kubelet docker -y')

for i in cluster_ip:
	commands.getoutput('sshpass -p redhat ssh '+i+' setenforce 0')
	commands.getoutput('sshpass -p redhat ssh '+i+' sed  -i   s/SELINUX=enforcing/SELINUX=disabled/g /etc/selinux/config')
	commands.getoutput('sshpass -p redhat ssh '+i+' systemctl enable --now firewalld')
	commands.getoutput('sshpass -p redhat ssh '+i+' firewall-cmd --add-port=0-65535/tcp  --permanent')
	commands.getoutput('sshpass -p redhat ssh '+i+' firewall-cmd --add-port=0-65535/udp  --permanent')
	commands.getoutput('sshpass -p redhat ssh '+i+' firewall-cmd --reload')
	commands.getoutput('sshpass -p redhat ssh '+i+' sed -i  / swap / s/^\(.*\)$/#\1/g /etc/fstab')
	commands.getoutput('sshpass -p redhat ssh '+i+' swapoff -a')
	commands.getoutput('sshpass -p redhat ssh '+i+' modprobe br_netfilter')
	commands.getoutput('sshpass -p redhat ssh '+i+' echo  "net.bridge.bridge-nf-call-ip6tables = 1" >>/etc/sysctl.conf')
	commands.getoutput('sshpass -p redhat ssh '+i+' sysctl -p')
	commands.getoutput('sshpass -p redhat ssh '+i+' systemctl enable --now docker ; systemctl enable kubelet')


	
	
	
	





















