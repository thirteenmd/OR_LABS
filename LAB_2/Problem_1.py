# -*- coding: utf-8 -*-
"""
Created on Mon May  1 23:18:06 2017

@author: Best
"""

c = [-18800, -24776, -10340] #the minimization of the -1*function is the maximization!
A = [ 
      [1, 1, 1],
      [0, -3240, -1660]
    ]
b = [1.2, -1500]

x0_bounds = (0.5, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

from scipy.optimize import linprog

result = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds, x2_bounds))

print(result)

profitPerYear = []