# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:24:49 2018

@author: kampa_000
"""

class Queue(object):
    def __init__(self):
        self.items=[]
    def enque(self,item):
        self.items.append(item)
    def deque(self):
        return self.items.pop(self.items[0])
    def display_queue(self):
        for i,val in enumerate(self.items):
            print(i,val)
q=Queue()
