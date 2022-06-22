#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BDGS: Binary Drop Growth Simulator
#
# See the README file in the top-level directory.

# -----------------------------------------------------------------------------
# This file (main.py) generates an equilibrium drop
# -----------------------------------------------------------------------------

# date         :22-Jun-22
# version      :0.1.0
# usage        :python3 main.py
# py_version   :3.8

# Initialize ==================================================================

# Dependencies
import pickle
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import sys

# Parameters and Initial configuration
with open('../nonequilibrium/data/drop.pkl','rb') as f:
    alpha,beta2,beta3,Rbinit,h1init,h2init,h3init = pickle.load(f)

# Variables
R1,R2,R3 = sym.symbols('R1,R2,R3')
h1,h2,h3 = sym.symbols('h1,h2,h3')
Rb = sym.symbols('Rb')

# Equations
eqn1 = {R1:(h1**2+Rb**2)/(2*h1),
        R2:(h2**2+Rb**2)/(2*h2),
        R3:(h3**2+Rb**2)/(2*h3)}
eqn2 = sym.Eq(R1**3-h1*(h1**2+3*Rb**2)/8-h3*(h3**2+3*Rb**2)/8,1)
eqn3 = sym.Eq(h2*(h2**2+3*Rb**2)/8+h3*(h3**2+3*Rb**2)/8,alpha)
eqn4 = sym.Eq(beta2/R2-1/R1,beta3/R3)
eqn2 = eqn2.subs(eqn1)
eqn3 = eqn3.subs(eqn1)
eqn4 = eqn4.subs(eqn1)
costh1 = (Rb**2-h1**2)/(Rb**2+h1**2)
costh2 = (Rb**2-h2**2)/(Rb**2+h2**2)
costh3 = (Rb**2-h3**2)/(Rb**2+h3**2)
eqn5 = sym.Eq(beta2*costh2+beta3*costh3-costh1,0)

# Equilibrium solution
sol = sym.nsolve([eqn2,eqn3,eqn4,eqn5],
                 (Rb,h1,h2,h3),
                 (Rbinit,h1init,h2init,h3init))
# print(sol)
Rbsol,h1sol,h2sol,h3sol=sol
R1sol=(h1sol**2+Rbsol**2)/(2*h1sol)
R2sol=(h2sol**2+Rbsol**2)/(2*h2sol)
R3sol=(h3sol**2+Rbsol**2)/(2*h3sol)

# Droplet shapes
th1 = np.arccos(np.double(1-h1sol/R1sol))
arc1 = np.linspace(th1,2*np.pi-th1,100)
x1 = (-R1sol+h1sol)+R1sol*np.cos(arc1)
y1 = R1sol*np.sin(arc1)
th2 = np.arccos(np.double(1-h2sol/R2sol))
arc2 = np.linspace(-th2,th2,100)
x2 = (-R2sol+h2sol)+R2sol*np.cos(arc2)
y2 = R2sol*np.sin(arc2)
th3 = np.arccos(np.double(1-h3sol/R3sol))
arc3 = np.linspace(-th3,th3,100)
x3 = (-R3sol+h3sol)+R3sol*np.cos(arc3)
y3 = R3sol*np.sin(arc3)

# Drop visualization
plt.figure(figsize=(8, 8))
plt.plot(y1,x1,color='green')
plt.plot(y2,x2,color='red')
plt.plot(y3,-x3,color='blue')
plt.gca().set_aspect('equal')
# plt.grid()
# plt.title('Rb = ...')
plt.axis('off')
plt.savefig('fig/drop.png')
plt.show()

# Export drop data
with open('data/drop.pkl','wb') as f:
    pickle.dump([alpha,beta2,beta3,Rbsol,h1sol,h2sol,h3sol], f)

# Exit ========================================================================
sys.exit()
