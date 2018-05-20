#!/usr/bin/python2
ip=[i for i in raw_input('Enter The Ip Addess: ').split('.')] #ip in stringFormat
#converting to integer 
lt_ip=[]
for i in range (len(ip)):
    lt_ip.append(int(ip[i]))
#print lt_ip
def binary(x):  #binary function to convert into binary
    binary=[]
    while(x!=0):
        binary.append(x%2)
        x=x//2
#print binary #Binary in reverse form
    if len(binary)<8:
        for i in range (8-len(binary)):
	        binary.append(0)
#print binary #Binary in 8-bit form
    binary.reverse()
    return binary #Binary in proper Form of 8-bit 
ip_bin=[] #To get IP Addess in binary
for i in lt_ip:
    ip_bin.append(binary(i))

sub=[i for i in raw_input('Enter The Subnet Mask: ').split('.')] #sub in stringFormat
#converting to integer 
lt_sub=[]
for i in range (len(sub)):
    lt_sub.append(int(sub[i]))
#print lt_sub
sub_bin=[] # To get SubNet Mask in Binary
for i in lt_sub:
    sub_bin.append(binary(i))
#print ip_bin
#print sub_bin
# For Network bit & Host bit
net_bit=0
for i in range(4):
    for j in range(8):
        if(sub_bin[i][j]==1):
            net_bit=net_bit+1
print"----------------"
print "Network_bit=",net_bit
host_bit=32-net_bit
print "Host Bit=",host_bit
print"----------------"
#Classification of Ip
def classes():
    if net_bit!=c:
        sub_net_bit=net_bit-c
	#print "It is Sub_netted by",sub_net_bit,"bit"
#Network-ID
    net_id=[]
    for i in range(4):
	net_id.append(lt_ip[i]&lt_sub[i])
    print "---------------------------------"
    print "Network-ID=",net_id
#Broadcast-ID
    bc_id=net_id[:]
    for i in range(4):
	a=0
	for j in range(8):
	    if sub_bin[i][j]==0:
		a=a+1
	bc_id[i]=net_id[i]+2**a-1
    print "Broadcast-ID=",bc_id
    print "---------------------------------"
#For Number of Host
    host=2**host_bit
    print "---------------------------------"
    print"Total Number of Host=",host
    usable_host=host-2
    print"Total Number of Usable Host=",usable_host
    print "---------------------------------"
# For Find Classes of Ip
if (lt_ip[0]>0)&(lt_ip[0]<127):
   # print "class A"
    c=8
    classes()
if (lt_ip[0]>127)&(lt_ip[0]<191):
    #print "class B"
    c=16
    classes()
if (lt_ip[0]>191)&(lt_ip[0]<224):
    #print "class C"
    c=24
    classes()
