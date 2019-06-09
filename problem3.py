#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
print("Numbers greater than 5")
y=[i for i in adhoc if i>5]
print(y)
print("Numbers less than or equal to 2")
x=[i for i in adhoc if i<=2]
print(x)

