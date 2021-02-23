# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:25:53 2020

@author: BloodShot
"""


h = 12
m = 39

def f(h, m):
    h1 = 12-(h%12)
    m1 = 12 - int(m/5)
    c = m%5
    m1 = m1*5 - c
    return str(h1) + str(m1)
s = f(h, m) 
print(s) 
    