#!/usr/bin/python3

import pyqrcode
from pyqrcode import QRCode
from googlesearch import search

urlist=[]
u=0
web=input("Enter your choice:  ")
for i in search(web,stop=3):
	urlist.append(i)
	print(i)

	url = pyqrcode.create(urlist[u])
	url.svg("qr"+str(u)+".svg", scale = 6)
	u+=1
file=input("enter name of .html file: ")

os.system('touch'+' '+file)
os.system('echo "<html><h1>QR code for your search:n </h1><body><img src="1.svg"><img src="2.svg"><img src="3.svg"></body></html>"'+file)
os.system('sudo mv '+file+' '+'/var/www/html/)
os.system('sudo mv 1.svg /var/www/html/)
os.system('sudo mv 2.svg /var/www/html/)
os.system('sudo mv 3.svg /var/www/html/)
