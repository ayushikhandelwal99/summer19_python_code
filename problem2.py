#!/usr/bin/python3


from googlesearch import search
web=input("Please enter topic:")

url=[]
for i in search(web,stop=10):
        url.append(i)


f=open('file.txt','a+')
for i in url:
	f.write(i+'\n')
f.seek(0)
print(f.read())
f.close()


