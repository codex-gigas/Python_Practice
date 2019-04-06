# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:22:34 2018

@author: kampa
"""
#import time as t
def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a

a=[j for j in map(int,input("Enter values separated by space: ").split(" "))]
obj=insertion_sort(a)
print(obj)
