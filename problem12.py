#!/usr/bin/python3

import pyqrcode
from pyqrcode import QRCode
from googlesearch import search

urlist=[]
u=0
web=input("Enter your choice:  ")
for i in search(web,stop=5):
	urlist.append(i)
	print(i)

	url = pyqrcode.create(urlist[u])
	url.svg("qr"+str(u)+".svg", scale = 6)
	u+=1
	print(url.terminal())

