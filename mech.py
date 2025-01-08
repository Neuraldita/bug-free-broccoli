#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 11:52:45 2024

@author: nandhithashri
"""

import numpy as np
import matplotlib.pyplot as plt

c = 3e8  
v = 5e14 
wavelength = c / v  
d0 = 0.5e-6 #initial mirror separation

# Reflectivity
R1 = 0.9
R2 = 0.2

# Range of x values 
x = np.linspace(-500e-9, 1500e-9, 5000)

#  new mirror separation
d = d0 + x

#  phase difference delta
delta = (4 * np.pi * d) / wavelength

# Transmission intensity  for a Fabry–Perot interferometer
def transmission_intensity(R):
    F = (4 * R) / ((1 - R) ** 2)
    I = 1 / (1 + F * np.sin(delta / 2) ** 2)
    return I

# Transmission intensities for both reflectivities
I_R1 = transmission_intensity(R1)
I_R2 = transmission_intensity(R2)

# Plot the results
plt.figure(figsize=(11, 5))
plt.plot(x * 1e9, I_R1, label='R = 0.9')
plt.plot(x * 1e9, I_R2, label='R = 0.2')
plt.xlabel('MIRROR SEPARATION ADJUSTMENT X (nm)')
plt.ylabel('TRANSMISSION INTENSITY I')
plt.title('TRANSMISSION INTENSITY VS MIRROR SEPARATION X')
plt.legend()
plt.grid(True)
plt.show()