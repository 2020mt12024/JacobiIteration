# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:05:10 2020

@author: SSMOHANTA
"""
import numpy as np

def JIteration(A,b,s,epsilon,N):
    n=A.shape[0]
    I = np.identity(n)
    x = np.ones(n)
    t = np.ones(n)
    print("A:")
    print(A)
    print("b:")
    print(b)
    print("Initial x:")
    print(s)
    for m in range(0, N):
        #print(np.dot(I-A,t).transpose())
        x = b + np.dot(I-A,t).transpose()
        print("Iteration: " + str(m+1))    
        print("x: ")
        print(x)
        #print("t: ")
        #print(t)
        if(max(abs(x-t)) < epsilon):
            print("Converged after " + str(m+1) +" Iteration")
            return x
        t[:] = x        
    return x