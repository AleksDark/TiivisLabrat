# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:42:09 2016

@author: sofiev
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:56:37 2016

@author: sofiev
"""

import os
os.chdir('/home/sofiev/University/TiivisLabrat/2GammasateilynVaimeneminen')

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt


sFile='N9_tausta/taustaCountingRateVsTime.txt'
N_tausta=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N_tausta=N_tausta[0:299]
print N_tausta.mean()



sFile='N0/taustaCountingRateVsTime.txt'
N0=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N0=N0[0:299]

sFile='N1/taustaCountingRateVsTime.txt'
N1=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N1=N1[0:299]

sFile='N2/taustaCountingRateVsTime.txt'
N2=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N2=N2[0:299]

sFile='N3/taustaCountingRateVsTime.txt'
N3=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N3=N3[0:299]

sFile='N4/taustaCountingRateVsTime.txt'
N4=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N4=N4[0:299]

sFile='N5/taustaCountingRateVsTime.txt'
N5=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N5=N5[0:299]

sFile='N6/taustaCountingRateVsTime.txt'
N6=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N6=N6[0:299]

sFile='N7/taustaCountingRateVsTime.txt'
N7=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N7=N7[0:299]

sFile='N8/taustaCountingRateVsTime.txt'
N8=np.loadtxt(sFile,skiprows=1,usecols=(1,))
N8=N8[0:299]
#%%
aAika=[300.48, 300.48, 300.16, 400.0, 301.12, 399.68, 399.68, 300.16, 300.48, 400.64]

dResults=[N0.mean()-N_tausta.mean()]
dResults.append( N1.mean()-N_tausta.mean())
dResults.append( N2.mean()-N_tausta.mean())
dResults.append( N3.mean()-N_tausta.mean())
dResults.append( N4.mean()-N_tausta.mean())
dResults.append( N5.mean()-N_tausta.mean())
dResults.append( N6.mean()-N_tausta.mean())
dResults.append( N7.mean()-N_tausta.mean())
dResults.append( N8.mean()-N_tausta.mean())

aStartThickness=[0,0.13,0.15,0.15,0.13,0.13,0.15,0.15,0.16]
adResultThickness=np.zeros([10,1])
#np.savetxt('Analysis/LyijynVaikutus.txt', dResults, newline=" ")
np.savetxt('Analysis/LyijynVaikutus.txt', dResults, newline="\n")

for i in range(9):
    adResultThickness[i]=sum(aStartThickness[0:i+1])


N=dResults;


#x=np.loadtxt(file,skiprows=1,usecols=(1,))
logN =np.log(N)

#x=np.zeros([10,1])
x=logN*0
for i in range(len(x)):
    x[i]=adResultThickness[i][0]


print('x= ',x)
print(N)
print('logN=',logN)
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
xp=np.linspace(0,1.5,500)  # tuottaa suoran xp

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
pl.title('Sateilyn vaimeneminen lyijyssa',size=18,fontweight='bold')
pl.xlabel('lyijyn paksuus (mm)',size=14)
pl.ylabel('log N (1/s)',size=14)

#pl.ion()
pl.show()
#pl.waitforbuttonpress(timeout=-1)


















##########################################
aErrors=np.zeros([1,10])
aErrors[0][0]=np.sqrt(((N0-N0.mean())**2).sum() /(len(N0))-1) /np.sqrt(len(N0))
aErrors[0][1]=np.sqrt(((N1-N1.mean())**2).sum() /(len(N1))-1) /np.sqrt(len(N0))
aErrors[0][2]=np.sqrt(((N2-N2.mean())**2).sum() /(len(N2))-1) /np.sqrt(len(N0))
aErrors[0][3]=np.sqrt(((N3-N3.mean())**2).sum() /(len(N3))-1) /np.sqrt(len(N0))
aErrors[0][4]=np.sqrt(((N4-N4.mean())**2).sum() /(len(N4))-1) /np.sqrt(len(N0))
aErrors[0][5]=np.sqrt(((N5-N5.mean())**2).sum() /(len(N5))-1) /np.sqrt(len(N0))
aErrors[0][6]=np.sqrt(((N6-N6.mean())**2).sum() /(len(N6))-1) /np.sqrt(len(N0))
aErrors[0][7]=np.sqrt(((N7-N7.mean())**2).sum() /(len(N7))-1) /np.sqrt(len(N0))
aErrors[0][8]=np.sqrt(((N8-N8.mean())**2).sum() /(len(N8))-1) /np.sqrt(len(N0))

aErrors[0][9]=np.sqrt(((N_tausta-N_tausta.mean())**2).sum() /len(N_tausta)) /np.sqrt(len(N_tausta))

print aErrors