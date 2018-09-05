# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:32:32 2018

@author: kampa_000
"""
i=1
a=[10,20,30,40,50]
for i in range(100):
    if i%2==0:
        if i==50:
            break
        if i in a:
            continue
        
        if i == 34:
            i=i+10
        print(i)