#!/usr/bin/python3

import socket
rev_IP = "127.0.0.1"
rev_port = 4444

#creating udp socket with ip type v4
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#fitting ip and port with socket
s.bind((rev_IP,rev_port))
schoice=s.recvfrom(10)#receiving choice of sender
c=schoice[0].decode('ascii')
if c == '1' :
	while 4 > 2 :
		data=s.recvfrom(100) #receiving message
		print("message is", data[0]) #printing message
		print("IP+port --> socket", data[1])
		#replying to sender
		rply=input("Type your reply")
		new = rply.encode('ascii')
		s.sendto(new,data[1])
	s.close()
elif c == '2' :
	while 4 > 2 :
		data=s.recvfrom(1500)
		ndata=data[0].decode('ascii')
		print("message is:  ",ndata)
else :
	print("Enter correct choice!!!")


