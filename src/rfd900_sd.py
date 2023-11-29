#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:34:12 2023

@author: Hasith Perera - KE8TJE
"""


import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

file = '../Data/RFD900/PAYLOAD.CSV.5';
df = pd.read_csv(file)


cols = ['Analog External','Analog Internal','Digital Internal','Digital External']

for col in cols:
    df[col] = df[col].astype(float)
    plt.plot(df[col])
    
plt.legend(cols)
plt.ylabel(r'$c$')
plt.xlabel(r'$time (s)$')






#
#
