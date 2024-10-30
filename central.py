# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:55:51 2024

@author: joahb
"""

import numpy as np 
import matplotlib.pyplot as plt

def function(x):
    return 2 + 0.75 * np.tanh(2 * x)
def derfun(x):
    return 1.5 * (1/np.cosh(2*x)**2) 

def centdef(h):
    derfunc = []
    for x in np.arange(-2, 2, 0.1):
        der = (function(x + h) - function(x - h)) / (2 * h)
        derfunc.append(der)
    return derfunc

x = np.arange(-2, 2, 0.1)
y = derfun(x)

plt.title('2 + 0.75*np.tanh(2*x)')
plt.xlabel("x values")
plt.ylabel("exact dereivative")
plt.grid(True)
plt.plot(x, y, "r", label="exact")

# Plot the derivatives with different values of h
plt.plot(x, centdef(1), "b--", label="approx h=1")
plt.plot(x, centdef(0.5), "g--", label="approx h=0.5")
plt.plot(x, centdef(0.1), "m--", label="approx h=0.1")

plt.legend(loc=2)
plt.show()