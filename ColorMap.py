#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:45:48 2019

@author: s1620023
"""

import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as pl
import re

#numbers = re.compile(r'(-?\d+)')
#def numericalSort(value):
#    parts = numbers.split(value)
#    parts[1::2] = map(int, parts[1::2])
#    return parts
#numbers = re.compile(r'-?\d+')
def NumericalSort (values):
    parts = re.findall(r'-?\d+\.\d+', values)
    parts[0] = float(parts[0])
    return parts

path = '/home/s1620023/ownCloud/PythonScript(ForTutorial)/DampedSineData/'
#files = glob.glob(path + r"/*Hz.csv")
files = sorted(glob.glob(path + r"/*Hz.csv"), key=NumericalSort)

ilist = [] 
fdlist = []
for f in files:
    Data = pd.read_csv(f)
    number = re.findall('-?\d+\.\d+',f)
    fd = float(number[0])
    i = np.array(Data['A'])
    ilist.append(i)
    fdlist.append(fd)

I = np.vstack(ilist)
t = np.array(Data['t'])
Fd = fdlist
Fd = sorted(Fd) 

Y, X = np.meshgrid(t, Fd)

pl.tick_params (length = 6.0)
pl.rc('text', usetex=True)
pl.rc('font', family = 'serif', size = 20)
pl.tick_params(labelsize = 20)
pl.xticks(fontsize = 20)
pl.yticks(fontsize = 20)

pl.xlabel(r'$f_d$ (Hz)', fontsize=20) #, fontname = 'Arial')
pl.ylabel(r'$t$ (s)', fontsize = 20)
pl.pcolormesh(X, Y, I)
pl.colorbar(label = r'A (norm.)')
pl.savefig(path + r"Chevron", dpi = 200, format = 'png', bbox_inches = 'tight', frameon = False)
pl.show()
#print(files)

