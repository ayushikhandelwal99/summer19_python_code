#!/usr/bin/python3

from googlesearch import search
import speech_recognition as sr

options = '''
Press 1 to type topic
Press 2 to for mic
'''
print(option)
choice = input("Enter your choice:")
url =[]
if choice == '1' :
	web=input("Please enter topic:")
	for i in search(web,stop=10):
        	url.append(i)
        f=open('urls.txt','a+')
	for i in url:
		f.write(i+'\n')
	f.seek(0)
	print(f.read())
	f.close()
elif choice == '2' :
	 r = sr.Recognizer()

     with sr.Microphone() as sorce:
         print("Enter your searh")
         audio=r.listen(source)
		print("search received")

         try:
             text = r.recognize_google(audio)
             print('You said : {}'.format(text) )

         except Exception as e:
             print(e)
else :
	print("Enter correct choice!!!!")

