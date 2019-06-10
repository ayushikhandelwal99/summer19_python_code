#!/usr/bin/python3

import webbrowser
import time
import subprocess
import os
option='''
Press  1 to start your vlc media player:
Press  2 to play your fav song in youtube:
Press  3 to searchsomething on google:
Press  4 to send whatsapp message to your fav number:
Press  5 to check current time and date:
Press  6 to reboot your machine:
'''

print(option)

choice=int(input())

if choice == 1 :
	subprocess.getoutput('vlc')
elif choice == 2 :
	webbrowser.open_new_tab('https://www.youtube.com/watch?v=wy2DgqL1P7s')
elif choice == 3 :
	data=input("type your search :--->  ")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)
elif choice == 4 :
	number=input("Enter your number with your country code:")
	webbrowser.open_new_tab('https://api.whatsapp.com/send?phone='+number)      
elif choice == 5 :
	current_time=time.ctime()
	print(current_time)
elif choice == 6 :
	os.system('reboot')
else :
	print("kuch nhi krna mujhe")
