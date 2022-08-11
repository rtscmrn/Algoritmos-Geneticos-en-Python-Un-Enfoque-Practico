#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:56:32 2022

@author: raultoscanomiranda.

"""

import random
print("Begining test")
def new_func():
    random.seed()
    x= [random.uniform(-100, 100) for i in range(10)]
    y= [random.uniform(-100, 100) for i in range(10)]
    print(x)
    print(y)

new_func()

import numpy as np
np.random.seed(0)

def new_func1():
    #generate
    x2 = np.random.uniform(-100, 100, 10).reshape(1, 10)
    y2 = np.random.uniform(-100, 100, 10).reshape(1, 10)
    print('x2:' , x2, 'y2: ', y2)

new_func1()


print("End")
