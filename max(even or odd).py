# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:15:16 2018

@author: kampa
"""

n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
for i in b:
    if(i%2==0):
        c.append(i)
        b.remove(i)
print(max(c))
print(max(b))
        