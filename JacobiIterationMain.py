# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:07:11 2020

@author: SSMOHANTA
"""
from JacobiIteration import JIteration

import numpy as np

A = np.array([[4.0,-1.0,0.0],[-1.0,4.0,-1.0],[0.0,-1.0,4.0]])
b = np.array([21.0,-45.0,33.0])
x0 = np.array([1.0,1.0,1.0])
epsilon = 1E-6
maxIter = 10
I = np.identity(3)
#print(np.linalg.eigvals(I-A/4))
x = JIteration(A/4,b/4,x0,epsilon,maxIter)


print(x)