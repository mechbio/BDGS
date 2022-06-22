#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BDGS: Binary Drop Growth Simulator
#
# See the README file in the top-level directory.

# -----------------------------------------------------------------------------
# This file (main.py) generates drop relaxing shape evolution
# -----------------------------------------------------------------------------

# date         :22-Jun-22
# version      :0.1.0
# usage        :python3 main.py 60 30
# py_version   :3.8

# Initialize ==================================================================

# Dependencies
import pickle
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import imageio
import os
import sys

# GIF parameters
n = int(sys.argv[1])
fps = int(sys.argv[2])

# Parameters and Initial configuration
with open('../nonequilibrium/data/drop.pkl','rb') as f:
    alpha,beta2,beta3,Rbinit,h1init,h2init,h3init = pickle.load(f)

# Variables
R1,R2,R3 = sym.symbols('R1,R2,R3')
h1,h2,h3 = sym.symbols('h1,h2,h3')
Rb = sym.symbols('Rb')
F = sym.symbols('F')

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
eqn5 = sym.Eq(beta2*costh2+beta3*costh3-costh1,F)

# Relaxation simulation
Rbsol = np.zeros(shape=(n,1))
h1sol = np.zeros(shape=(n,1))
h2sol = np.zeros(shape=(n,1))
h3sol = np.zeros(shape=(n,1))
R1sol = np.zeros(shape=(n,1))
R2sol = np.zeros(shape=(n,1))
R3sol = np.zeros(shape=(n,1))

costh1init = (Rbinit**2-h1init**2)/(Rbinit**2+h1init**2)
costh2init = (Rbinit**2-h2init**2)/(Rbinit**2+h2init**2)
costh3init = (Rbinit**2-h3init**2)/(Rbinit**2+h3init**2)
Finit = float(beta2*costh2init+beta3*costh3init-costh1init)
Flist = np.linspace(Finit,0,n)
for i in tqdm(range(n)):
    # Initial state
    if i == 0:
        Rbsol[i] = Rbinit
        h1sol[i] = h1init
        h2sol[i] = h2init
        h3sol[i] = h3init
        R1sol[i]=(h1sol[i]**2+Rbsol[i]**2)/(2*h1sol[i])
        R2sol[i]=(h2sol[i]**2+Rbsol[i]**2)/(2*h2sol[i])
        R3sol[i]=(h3sol[i]**2+Rbsol[i]**2)/(2*h3sol[i])
        continue
    # Quasi-static equilibrium states
    sol = sym.nsolve([eqn2,eqn3,eqn4,eqn5.subs({F:Flist[i]})],
                     (Rb,h1,h2,h3),
                     (float(Rbsol[i-1]),float(h1sol[i-1]),
                      float(h2sol[i-1]),float(h3sol[i-1])))
    Rbsol[i],h1sol[i],h2sol[i],h3sol[i]=sol
    R1sol[i]=(h1sol[i]**2+Rbsol[i]**2)/(2*h1sol[i])
    R2sol[i]=(h2sol[i]**2+Rbsol[i]**2)/(2*h2sol[i])
    R3sol[i]=(h3sol[i]**2+Rbsol[i]**2)/(2*h3sol[i])

# Drops shapes
m = 100
x1 = np.zeros(shape=(n,m))
y1 = np.zeros(shape=(n,m))
x2 = np.zeros(shape=(n,m))
y2 = np.zeros(shape=(n,m))
x3 = np.zeros(shape=(n,m))
y3 = np.zeros(shape=(n,m))

for i in tqdm(range(n)):
    # Droplet shapes
    th1 = np.arccos(np.double(1-h1sol[i]/R1sol[i]))
    arc1 = np.linspace(th1,2*np.pi-th1,m)
    x1[i] = (-R1sol[i]+h1sol[i])+R1sol[i]*np.cos(arc1)
    y1[i] = R1sol[i]*np.sin(arc1)
    th2 = np.arccos(np.double(1-h2sol[i]/R2sol[i]))
    arc2 = np.linspace(-th2,th2,m)
    x2[i] = (-R2sol[i]+h2sol[i])+R2sol[i]*np.cos(arc2)
    y2[i] = R2sol[i]*np.sin(arc2)
    th3 = np.arccos(np.double(1-h3sol[i]/R3sol[i]))
    arc3 = np.linspace(-th3,th3,m)
    x3[i] = (-R3sol[i]+h3sol[i])+R3sol[i]*np.cos(arc3)
    y3[i] = R3sol[i]*np.sin(arc3)

# Evolution GIF frames
pngs = []

for i in tqdm(range(n)):
    # Drop visualization
    plt.figure(figsize=(8, 8))
    plt.plot(y1[i],x1[i],color='green')
    plt.plot(y2[i],x2[i],color='red')
    plt.plot(y3[i],-x3[i],color='blue')
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    png = f'fig/drop_{i:02}.png'
    pngs.append(png)
    plt.savefig(png)
    plt.close()

# GIF frames
frames = []
for png in tqdm(pngs):
    frame = imageio.v2.imread(png)
    frames.append(frame)

# make GIF
imageio.mimsave('fig/drop.gif',frames,fps=fps)

for png in tqdm(set(pngs)):
    # remove PNGs
    os.remove(png)

# Export equilibrium drop data
with open('data/drop.pkl','wb') as f:
    pickle.dump([alpha,beta2,beta3,
                 Rbsol[n-1],h1sol[n-1],h2sol[n-1],h3sol[n-1]], f)

# Exit ========================================================================
sys.exit()
