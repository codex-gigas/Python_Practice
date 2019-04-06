# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:00:21 2018

@author: kampa
"""

n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
(r,c,d)=(0,0,0)
for i in b:
    if(i<0):
        r=r+i
    elif(i%2==0):
        c=c+i
    else:
        d=d+i
print("sum of negative numbers: ", r)
print("sum of positive even numbers: ", c)
print("sum of positive odd numbers: ", d)