# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:43:37 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon_0 = 8.854e-12  # permittivity of free space
q1 = 1  # charge in Coulombs
q2 = -1  # charge in Coulombs
rp1 = np.array([-0.05, 0])  # position of q1
rp2 = np.array([0.05, 0])  # position of q2
min_distance = 0.001  # minimum distance to avoid singularity

# Set up the grid
x = np.arange(-0.1, 0.1, 0.001)
y = np.arange(-0.1, 0.1, 0.001)
X, Y = np.meshgrid(x, y)

# Define a function to calculate r and V at each point
def calculate_potential(xp, yp, q):
    r = np.sqrt((X - xp)**2 + (Y - yp)**2)
    r = np.maximum(r, min_distance)  # Set minimum distance to avoid infinity
    V = q / (4 * np.pi * epsilon_0 * r)
    return V

# Calculate potentials due to each charge and sum them
V1 = calculate_potential(rp1[0], rp1[1], q1)
V2 = calculate_potential(rp2[0], rp2[1], q2)
V = V1 + V2  # total potential

# Plot the potential
plt.figure()
plt.contourf(X, Y, V, levels=1000, cmap='RdYlBu')
plt.colorbar(label="Potential (V)")
plt.title("Electric Potential of Two Opposite Charges")
plt.ylim(-0.005,0.005)
plt.xlim(-0.065,0.065)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("potential.png")
plt.show()

# Calculate electric field as the negative gradient of the potential
Ey, Ex = np.gradient(-V, y, x)  # Note: np.gradient returns (y, x) gradients

# Plot the electric field using quiver
plt.figure()
plt.quiver(X, Y, Ex, Ey, color='black', scale=5e15)  # Adjust the scale as needed
plt.title("Electric Field of Two Opposite Charges")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("efield.png")
plt.show()