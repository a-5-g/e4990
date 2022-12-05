# -*- coding: utf-8 -*-
"""na_hw5_6ii.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qQQLVOFRgYi3Qi0BVRTW6wtwREIxyLli
"""

import numpy as np
from numpy import linalg as LA

def f(x):
  return 2*pow(x[0],2) + 3*pow(x[1],2) + 4*pow(x[2],2) + 2*x[0]*x[1] - 2*x[0]*x[2] - 8*x[0] - 4*x[1] - 2*x[2]

def grad(x):
  g1 = 4*x[0] + 2*x[1] - 2*x[2] - 8
  g2 = 6*x[1] + 2*x[0] - 4
  g3 = 8*x[2] - 2*x[0] - 2
  return np.array([g1, g2, g3], dtype = np.float64)

A = np.array([[4, 2, -2], [2, 6, 0], [-2, 0, 8]])
B = np.matmul(A.T, A)
e, v = LA.eigh(B)
k = np.amax(e)
L = np.sqrt(k)
tk = 1/L

def gradproj(x0):
  iter = 0
  xk = x0
  xk1 = x0
  for iter in range(1,101):
    temp = xk - tk * grad(xk)
    for j in range(0,3):
      temp[j] = max(0, temp[j])
    xk1 = temp
    xk = xk1
    print(f"Value of the function at iteration number {iter} is: {f(xk)}")
  return xk1

x0 = np.zeros(3)
ans = gradproj(x0)
print(f"The value of the function after 100 iterations is: {f(ans)}")
print("The produced solution is: ", ans)


