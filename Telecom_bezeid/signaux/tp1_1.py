#!usr/bin/Python
#-*- coding ; utf-8 *-*

import math
import matplotlib.pyplot as plt
#from scipy.signal.wavefroms import sawtooth, square
import numpy as np

def make_sin(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    """
    Create a synthetic 'sine wave'
    First version : use classic python lists
    """
    """
    a : c'est l'intervale du voltage (la longueur de l'amplitude) 
    f : la frequence du temps entre deux points
    fe: la frequence d'echantillons 
    nT : le nombre de periodes
    
    #signaux en "opposition de phase" dephases de 180
    a1=1.5
    a2=1.5
    ph1=0;
    ph2=math.pi    (dephases de 180)
    f1=f2=50.0 Hz 
    fe1=500
    fe2=1000
    
    c) la frequence d'echantillon pour les deux signaux est differente
    """
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    sig_t = []
    sig_s = []
  
    for i in range(int(N*nT)):
        t = te*i
        sig_t.append(t)
        sig_s.append(a*math.sin((omega*t)+ph))
    return sig_t, sig_s

def plot(inx, iny, inx2, iny2, title,format1, format2):
    plt.plot(inx,iny,format1,inx2,iny2,format2)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    #plt.ylim([-1.2, +1.2])
    plt.grid(True)

    
if __name__ == '__main__':
    x,y=make_sin(1.5,f=50.0,fe=500,nT=2.5)
    x2,y2=make_sin(0.5,ph=math.pi,f=50.0,fe=1000,nT=2.5)
    plot(x,y,x2,y2,"Deux cosinusoide ...",'bo','r.')
    
    plt.show()
