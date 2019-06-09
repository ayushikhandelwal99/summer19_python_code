#!/usr/bin/python3

import datetime

name=input("Enter your name:")
c_hr=datetime.datetime.now().hour

if c_hr<12:
	print("Good Morning "+name+" :)")
elif c_hr>=12 and c_hr<17:
	print("Good Afternoon "+name+" :)")
elif c_hr>=17 and c_hr<21:
	print("Good Evening "+name+" :)")
else:
	print("Good Night "+name+" :)")

