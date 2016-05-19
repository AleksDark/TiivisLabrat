# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:56:37 2016

@author: sofiev
"""

import os
os.chdir('/home/sofiev/University/TiivisLabrat/2GammasateilynVaimeneminen')

import numpy as np
import pylab as pl


sFile='N9_tausta/taustaCountingRateVsTime.txt'
N_tausta=np.loadtxt(sFile,skiprows=1,usecols=(1,))

print N_tausta.mean()



sFile='N0/taustaCountingRateVsTime.txt'
N0=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N1/taustaCountingRateVsTime.txt'
N1=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N2/taustaCountingRateVsTime.txt'
N2=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N3/taustaCountingRateVsTime.txt'
N3=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N4/taustaCountingRateVsTime.txt'
N4=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N5/taustaCountingRateVsTime.txt'
N5=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N6/taustaCountingRateVsTime.txt'
N6=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N7/taustaCountingRateVsTime.txt'
N7=np.loadtxt(sFile,skiprows=1,usecols=(1,))

sFile='N8/taustaCountingRateVsTime.txt'
N8=np.loadtxt(sFile,skiprows=1,usecols=(1,))

#%%
aAika=[300.48, 300.48, 300.16, 400.0, 301.12, 399.68, 399.68, 300.16, 300.48, 400.64]

dResults=[N0.mean()/aAika[0]-N_tausta.mean()/aAika[9]]
dResults.append( N1.mean()/aAika[1]-N_tausta.mean()/aAika[9])
dResults.append( N2.mean()/aAika[2]-N_tausta.mean()/aAika[9])
dResults.append( N3.mean()/aAika[3]-N_tausta.mean()/aAika[9])
dResults.append( N4.mean()/aAika[4]-N_tausta.mean()/aAika[9])
dResults.append( N5.mean()/aAika[5]-N_tausta.mean()/aAika[9])
dResults.append( N6.mean()/aAika[6]-N_tausta.mean()/aAika[9])
dResults.append( N7.mean()/aAika[7]-N_tausta.mean()/aAika[9])
dResults.append( N8.mean()/aAika[8]-N_tausta.mean()/aAika[9])

aStartThickness=[0,0.13,0.15,0.15,0.13,0.13,0.15,0.15,0.16]
adResultThickness=0
#np.savetxt('Analysis/LyijynVaikutus.txt', dResults, newline=" ")
np.savetxt('Analysis/LyijynVaikutus.txt', dResults, newline="\n ")