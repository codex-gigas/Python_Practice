# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:26:41 2018

@author: kampa_000
"""

num=10
num1 = input("Enter numbers with spaces: ")
num2 = num1.split(" ")
total_sum = 0
for n in num2:
    total_sum = total_sum + int(n)
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
for i in num2:
    if int(avg)>int(i):
        print(i)