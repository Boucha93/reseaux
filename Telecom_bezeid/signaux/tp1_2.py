'''
Created on 4 fevr. 2014

@author: yezide
'''
#!usr/bin/Python
#-*- coding ; utf-8 *-*

import math
import matplotlib.pyplot as plt
#from scipy.signal.wavefroms import sawtooth, square
import numpy as np
from math import floor

def make_carre(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
    """
    Create a synthetic 'sine wave'
    First version : use classic python lists
    """
    """
    a : c'est l'intervale du voltage (la longueur de l'amplitude) 
    f : la frequence du temps entre deux points
    fe: la frequence d'echantillons (le nombre de points apparu dans le graphe)
    nT : le nombre de sommnets
    """
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    sig_t = []
    sig_s = []
    for i in range(N*nT):
        t = te*i
        sig_t.append(t)
        if(a*math.sin((omega*t)+ph)>0):
            sig_s.append(a)
        elif(a*math.sin((omega*t)+ph)<0):
            sig_s.append(-a)
        else:
            sig_s.append(0)
        
    return sig_t, sig_s


def make_DentDeScie(a=1.0, ph=0, f=440.0, fe=8000.0, nT=2):
 
    N = int(fe/f)
    te = 1.0/fe
    T=1/f
    sig_t = []
    sig_s = []
    for i in range(N*nT):
        t = te*i   # le temps par seconde variant entre 0 et 4
        sig_t.append(t)
        sig_s.append(2*a*((t/T)-math.floor(t/T)-0.5)) #voltage vairiant de entre 1 et 3
    return sig_t, sig_s

def make_triangle(a=1.0, ph=0, f=440.0, fe=8000.0, nT=1):
 
    omega = 2*math.pi*f
    N = int(fe/f)
    te = 1.0/fe
    T=1/f
    print(T)
    sig_t = []
    sig_s = []
    for i in range(N*nT):
        t = te*i    # le temps par seconde variant entre 0 et 4
        sig_t.append(t)
        sig_s.append(a*(4* abs((t/T) - math.floor((t/T)+0.5))-1.0))
    return sig_t, sig_s
  

def plot(inx, iny, title, format='-bo'):
    plt.plot(inx,iny,format)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    plt.xlim(0,0.05)
    plt.grid(True)
    
if __name__ == '__main__':
    x,y=make_DentDeScie(2,f=50.0,fe=1000.0,nT=3)
    plot(x,y,"Un Triangle ...")
    
    #plt.show()
