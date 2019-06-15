#!/usr/bin/python3

import socket

rev_IP = "127.0.0.1"
rev_port = 4444

#creating udp socket with ip type v4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

options='''
Press 1 for sending and receiving messages from both sides
Press 2 for sending file only from sender and receiving only from receiver
'''
y=print(options)
choice = input()
s.sendto(choice.encode('ascii'),(rev_IP,rev_port))
if choice == '1' :
	while 4 > 3 :
		msg = input("Enter your message: ")
		new = msg.encode('ascii') #converting the msg to bytes
		s.sendto(new,(rev_IP,rev_port))  #sending message
		print(s.recvfrom(100))  #printing received message
elif choice == '2' :
	while 4 > 3 :
		files=str(input("enter the file location"))
		f=open(files,'r')
		f.seek(0)
		msg=f.read()
		#sending data to target
		new=msg.encode('ascii')
		s.sendto(new,(rev_IP,rev_port))
		
else :
	print("Enter correct choice!!!")	
