#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:36:28 2019

@author: s1620023

This program generate Damped Sine data
"""

import numpy as np
from numpy import exp, cos, pi, sqrt
import matplotlib.pyplot as pl
import pandas as pd
from matplotlib import rc

path = r'/home/s1620023/ownCloud/PythonScript(ForTutorial)/'
filename = r'DampedSine_Detuned'

def DampedSine(A, f, t, fd):
    return A*(cos(2*pi*sqrt(f**2+fd**2)*t)) * exp(-G*t)
Fd = np.linspace(-10, 10, 500)

for i in Fd:
    A = 1
    t = np.linspace(0, 2, 500)
    f = 3
    fd = i
    G = .7
    rc('text', usetex = True)
    rc('font', family = 'serif', size = 20)
    #pl.xlabel('t (s)', fontsize = 20)
    #pl.ylabel('A (norm.)', fontsize = 20)
    y = DampedSine(A, f, t, fd)
    #pl.plot(t, y/y.max(), 'ro', lw = 3.0)
    #pl.show()
    #pl.close()
    data_frame = {'t':t, 'A':y}
    df = pd.DataFrame(data_frame, columns = ['t', 'A'])
    df.to_csv(path+'DampedSineData/'+filename+str(fd)+'Hz'+'.csv', mode='a', header=True)