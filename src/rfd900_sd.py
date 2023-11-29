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


cols = ['Analog External','Analog Internal','Digital Internal','Digital External',
        'Accel A', 'Accel Y', 'Accel Z',
        'Latitude', 'Longitude',
        'Battery',
        ]

print(df.keys())

# change data type 
for col in cols:
    df[col] = df[col].astype(float)
    
    

plt.figure(1)
for col in cols[0:4]:
    plt.plot(df[col])
    
    
plt.legend(cols)
plt.ylabel(r'$Temp (C^\degree)$')
plt.xlabel(r'$time (s)$')


plt.figure(2)
plt.title('Acc x,y,z')
for col in cols[4:7]:
    plt.plot(df[col])
    
plt.xlabel('time (s)')
    
    
plt.figure(3)
plt.title('lon/lat')

for col in cols[7:]:
    plt.plot(df[col])
    
plt.xlabel('time (s)')
    
    
# battery decay curve
plt.figure(4)
plt.plot(df['Battery'],'.')
plt.ylabel('Voltage (V)')
plt.xlabel('time (s)')