# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:45:55 2018

@author: kampa
"""

def towers_of_honoi(height,A,B,C):
    if height>=1:
        towers_of_honoi(height-1,A,C,B)
        move(A,B)
        towers_of_honoi(height-1,C,B,A)

def move(tf,tm):
    print("moving disk from ", tf , "to " , tm )
    
towers_of_honoi(3,'X','Y','Z')