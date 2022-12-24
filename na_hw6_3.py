# -*- coding: utf-8 -*-
"""na_hw6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDIjfHUngK9AeGQWXk1XBs-UKuSEJSvP
"""

import numpy as np
from scipy.optimize import fsolve

def eqs (p):
  x1,x2,x3, mu, l = p
  eq1 = 1 + mu + 2*l*x1
  eq2 = -4 + 2*mu + 2*l*x2
  eq3 = 1 + 2*mu + 2*l*x3
  eq4 = x1+ 2*x2 + 2*x3 + 2
  eq5 = x1**2 + x2**2 + x3**2 - 1
  return [eq1, eq2, eq3, eq4, eq5]

x1, x2, x3, mu, l = fsolve(eqs, (1,1,1,1,1))
def f(x1,x2,x3):
  return x1 - 4*x2 + x3

ans = f(x1,x2,x3)

print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
print(f"mu = {mu}, lambda = {l}")
print(f"The optimal solution is: {ans}")
