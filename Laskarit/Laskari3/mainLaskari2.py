#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on Wed May 18 09:53:24 2016

@author: sofiev
"""


import os ; # os.system('clear')
import numpy as np
import pylab as pl

os.chdir('/home/sofiev/University/TiivisLabrat/Laskarit/Laskari2')

file='data2.txt'

r=np.loadtxt(file,skiprows=1,usecols=(0,))
N=np.loadtxt(file,skiprows=1,usecols=(1,))


import numpy as np
import matplotlib.pyplot as plt

# read data from file
#xdata, ydata = np.loadtxt('wavePulseData.txt', unpack=True)

# create x and y arrays for theory
#x = np.linspace(-10., 10., 200)
#y = np.sin(x) * np.exp(-(x/5.0)**2)

# create plot
#plt.figure(1, figsize = (5,4) )
##plt.plot(x, y, 'b-', label='theory')
##plt.plot(xdata, ydata, 'ro', label="data")
#plt.plot(1/(r*r), N, 'ro', label="data")
#plt.xlabel('r')
#plt.ylabel('N')
#plt.legend(loc='upper right')
#plt.axhline(color = 'gray', zorder=-1)
#plt.axvline(color = 'gray', zorder=-1)

# save plot to file
#plt.savefig('WavyPulse.pdf')

# display plot on screen
#####plt.show()


x=1/(r*r);
aParameters=np.polyfit(x,N,1)

p = np.poly1d(aParameters)
xp=np.linspace(0,0.3, 100)
#plt.figure(2,figsize=(16,10))
#rSuora=plt.plot(x, N, 'ro', label='Data')
#rSuora2=plt.plot(xp, p(xp), '-', label='Sovitettu suora, \n $N=1/r^2$ *'+str(int(aParameters[0]*100)/100.0)+'+'+str(int(aParameters[1]*100)/100.0))
#
#pl.title('AOL 1.L2. teht. 1, Sateily kaanteisen etaisyyden nelion funktiona',size=20,fontweight='bold')
#pl.xlabel('$1/etaisyys^2 (1/cm^2)$',size=16)
#pl.ylabel('Naytteita minuutissa, (1/min) ',size=14)
#pl.legend([rSuora, rSuora2],['qweqwe','13123'])
#plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0., prop={'size':20})
#
#
#plt.savefig('1.png')
#plt.show()
print 'Parameters: ', aParameters

############################################## b part
#%%
aDifference=N-p(x)
aDiff2=aDifference*aDifference

import scipy
import scipy.stats
q=scipy.stats.chisquare(aDiff2)
print q

sigma2=sum(1.0/(len(N)-2)*aDiff2)
print sigma2
print 'Sigma', np.sqrt(sigma2)
#plt.figure(3,figsize=(6,4))
#plt.plot(sigma2, range(len(sigma2)),'.')




# display plot on screen
#plt.show()

dSigma=np.sqrt(sigma2);

x=1/(r*r);

# Sovitusparametrien epatarkkuuden laskeminen
D=(1/(dSigma*dSigma))*len(x)*sum(x**2/dSigma**2)-(sum(x/dSigma**2))**2
#D=(1/(dSigma*dSigma))*len(N)*sum(N**2/dSigma**2)-(sum(N/dSigma**2))**2
print D

sigmaA2=1/D *sum((x/dSigma)**2)
sigmaA=np.sqrt(sigmaA2)
print 'Sigma A:t : ', sigmaA2, dSigma
print 'Sigma A on vakion epatarkkuus'

sigmaB2=1/D*(len(x)/dSigma**2)
sigmaB=np.sqrt(sigmaB2);
print 'Sigma B:t : ', sigmaB2, sigmaB
print 'Sigma B on kulmakertoimen epatarkkuus'

a=1/D *(sum((x/dSigma)**2)*sum(N/dSigma**2)-sum(x/dSigma**2)*sum(x*N/dSigma**2))
print 'Vakio on a: ', a

# Suoran sovitus
aParameters=np.polyfit(x,N,1)


print 'Suoran parametrit', aParameters
#
p = np.poly1d(aParameters)
xp=np.linspace(0,0.3, 100)
plt.figure(2,figsize=(25,13))
rSuora=plt.plot(x, N, 'r.', label='Data')
rSuora2=plt.plot(xp, p(xp), '-', label='Sovitettu suora, \n $N=1/r^2$ * ('+str(int(aParameters[0]*100)/100.0)+'$\pm$'+str(int(100*sigmaB)/100.0)+') +'+str(int(aParameters[1]*100)/100.0) +'$\pm$'+str(int(100*sigmaA)/100.0)+')')
plt.errorbar(x,N, fmt='r.', xerr=0, yerr=dSigma, ecolor='black', capthick=3)
pl.title('AOL 1, L2, teht.2, Sateily kaanteisen etaisyyden nelion funktiona',size=28,fontweight='bold')
pl.xlabel('$1/etaisyys^2 (1/cm^2)$',size=18)
pl.ylabel('Naytteita minuutissa, (1/min) ',size=16)
pl.legend([rSuora, rSuora2],['qweqwe','13123'])
plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0., prop={'size':24})


#plt.show()
plt.savefig('2.png')
print 'Parameters: ', aParameters
print 'D', D
print sigmaA, sigmaB


#%% Tehtava 3
aSigma=np.sqrt(N);

bParameters=np.polyfit(x,N,1, w=1/aSigma)
p2 = np.poly1d(bParameters)

# Sovitusparametrien epatarkkuuden laskeminen
D=sum(1/(aSigma*aSigma))*sum(x**2/aSigma**2)-(sum(x/aSigma**2))**2
#D=(1/(dSigma*dSigma))*len(N)*sum(N**2/dSigma**2)-(sum(N/dSigma**2))**2
print D

sigmaA2=1/D *sum((x/aSigma)**2)
sigmaA=np.sqrt(sigmaA2)
print 'Sigma A:t : ', sigmaA2, sigmaA
print 'Sigma A on vakion epatarkkuus'

#
sigmaB2=1/D*sum(1/aSigma**2)
sigmaB=np.sqrt(sigmaB2);
print 'Sigma B:t : ', sigmaB2, sigmaB
print 'Sigma B on kulmakertoimen epatarkkuus'


plt.figure(3,figsize=(20,10))

#rSuora=plt.plot(x, N, '.', xp, p2(xp), '-', label='asdasd')
rSuora,=plt.plot(x, N, 'r.',label='Data')
rSuora2=plt.plot(xp, p2(xp), '-', label='Sovitettu suora, \n $N=1/r^2$ * ('+str(int(bParameters[0]*100)/100.0)+'$\pm$'+str(int(100*sigmaB)/100.0)+') +'+str(int(bParameters[1]*100)/100.0) +'$\pm$'+str(int(100*sigmaA)/100.0)+')')

plt.errorbar(x,N, fmt='r.', xerr=0, yerr=aSigma, ecolor='black', capthick=3)
pl.title('AOL 1.2.L2, Sateily kaanteisen etaisyyden nelion funktiona',size=28,fontweight='bold')
pl.xlabel('$1/etaisyys^2 (1/cm^2)$',size=18)
pl.ylabel('Naytteita minuutissa, (1/min) ',size=16)
pl.legend([rSuora, rSuora2],['qweqwe','13123'])
plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0., prop={'size':20})

#plt.show()
plt.savefig('3.png')
print 'Parameters, weighted fit: ', bParameters



#a=1/D *(sum((x/dSigma)**2)*sum(N/dSigma**2)-sum(x/dSigma**2)*sum(x*N/dSigma**2))
#print 'Vakio on a: ', a

