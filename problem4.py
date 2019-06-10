#!/usr/bin/python3

import os
import crypt

name=input("enter a user name containing only characters: ")
flag=0
num=[0,1,2,3,4,5,6,7,8,9]
for i in name:
        if i in str(num):
                flag=1

if(flag==1):
        print("Enter a valid user!!!")
else:
        usrpass = crypt.crypt("hello"+name,"176")
        os.system("useradd -p "+usrpass+" "+name)
        print("user "+name+" created")
~                                        
