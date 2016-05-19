# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:49:22 2016

@author: sofiev
"""

import os ; os.system('clear')
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math

#datan lukeminen N=kvantteja sekunnissa, x=lyijyn paksuus
file='lab12PlotData.txt'


N=np.loadtxt(file,skiprows=1,usecols=(0,))
x=np.loadtxt(file,skiprows=1,usecols=(1,))
logN =np.log(N)

print('x= ',x)
print(N)
print('logN'=logN)
# def rFunk on 1/r^2
#def rFunk(x):
#	return 1/r**2
#uusiR=rFunk(r)

#PLOTTAUS data N(x)
#pl.plot(N,x,'ob')

#Plottaus vol2, missä muuttuja logN = log(N)
#pl.plot(x,logN,'oy')

#Suoransovitus: parametrin (x-akseli,y-akseli, suoran aste)
#Polyfit tuottaa listan arvoista jotka sopivat

zParametrit = np.polyfit(x,logN, 1)#katsoo parametrit
p = np.poly1d(zParametrit)
xp=np.linspace(0,12,500)  # tuottaa suoran xp

plt.plot(x,logN,'.',xp,p(xp),'-')

#virhearviointi virheenneliö sig^2 = 1/(N-2)*sum(ali)

#def ali(y,a,b,x):
#    return(y-a-b*x)**2


#a=zParametrit[1]
#b=zParametrit[0]
#lasketaan virhe sig

#sig=ali(N,a,b,uusiR)
#summa=sum(sig)
#virhe=math.sqrt(summa/8)


#virheistä tehtiin luettol .txt ja nyt luetaan
#fileVirhe= 'virhe.txt'
#yErr=np.loadtxt(fileVirhe,skiprows=1,usecols=(0,))
#Virhepalkkien plottaus

#pl.plot(uusiR,N,'.')

#pl.errorbar(uusiR,N,yErr,0,'.')
#plt.plot(uusiR,N,'.',xp,p(xp),'-')
#KUVANMUOKKAUS
pl.title('Säteilyn vaimeneminen lyijyssä',size=18,fontweight='bold')
pl.xlabel('lyijyn paksuus (mm)',size=14)
pl.ylabel('log N (1/s)',size=14)

pl.ion()
pl.show()
pl.waitforbuttonpress(timeout=-1)

