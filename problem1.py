#!/usr/bin/python3

import datetime 
name=input("Enter your name:")
age=int(input("Enter your age:"))

c_year=int(datetime.datetime.now().year)

year=(95-age)+c_year

print(name+" you will turn 95 by the year ")
print(year)

