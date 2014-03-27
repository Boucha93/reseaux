#!usr/bin/python
#-*- coding: utf-8 *-*

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import tp1_1

""" Quantificateur sur b bits d'un signal sig_s
    d amplitude max vmax
    Cette fonction rend le signal quantifie 
    et le bruit sur chaque echantillon.
    """
def QS(sig_s, vmax, b):
    z=[]
    err=[]
    pasQ=(2*vmax)/pow(2,b)  #le pas entre les palliers rouge
    for i in range(len(sig_s)):
        if(sig_s[i]!=vmax):
            z.append(pasQ*(math.floor(sig_s[i]/pasQ)+0.5))
            
        else:
            z.append(pasQ*(math.floor(sig_s[i]/pasQ)-0.5))
           
        err.append(math.fabs(sig_s[i]-z[i]))
   
    
    """le z représente le quantize et le err représente le bruit de quantification
                    c-à-d la différence d'amplitude entre la valeur vraie et la valeur quantifiée correspondante"""
    return z, err  



# Convertit un nombre décimal (denier, base 10) entier en une chaîne binaire (base 2)

def  Denary2Binary (n,bit):
    '' 'Convertir l\'entier n à une chaîne binaire Bstr'''
    Bstr = ''
    signe= "0" #on rajoute zero si le signe est positive
    if(n<0):
        n=-n     #"doit être un entier positif"
        signe="1" #on rajoute 1 car le signe est negatif
   # if(n==0):  return  '0'
        
    while(n >  0): 
        Bstr = str ( n %  2 )  + Bstr
        n = n >>  1
    while (len(Bstr)<=bit):
        if(len(Bstr)==0):
            Bstr='000'+Bstr
        elif(len(Bstr)==1):
            Bstr='00'+Bstr
        else:
            Bstr='0'+Bstr
            
        bit=bit-1
    return signe+Bstr

def MSE(x,xq):
    N=len(x)
    res=0
    for i in range(N):
        res+=math.pow(x[i]-xq[i], 2)
    return res/N
"""cette fonction renvoie Le rapport signal sur bruit"""                 
def SNR(var,err):
    return (10*math.log10(var/err)) #valeur en decible :10 fois le logarithme decimal du rapport var,err

def variance(x):
    var=0
    N=len(x)
    for i in range(N):
        var+=pow(x[i],2)
    return var/N
 
def plot(inx, iny, title, fmt='-bo', l=""):
    plt.plot(inx,iny,fmt,label=l)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.title(title)
    plt.ylim([-5.5, +5.5])
    plt.grid(True)
    
if __name__ == '__main__':
    np.set_printoptions(linewidth=250) 
    np.set_printoptions(precision=3, suppress=True)
    a=5.0
    b=4
    step = 2*a/(2**b)
  
    fe = 2000
    f = 50.0
    nT=1
    x,y=tp1_1.make_sin(a,0,f=f,fe=fe,nT=nT)
    
    #print y
    #y = np.array(y)+a
    z,err = QS(y,a,b)
    # plot du signal quantifie
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(1,1,1)
    majorLocator = MultipleLocator(step)
    ax.yaxis.set_major_locator(majorLocator) 
    plot(x,y,"",'bo', l="Signal")
    plot(x,z,"",'rs', l="Quantized")
    plot(x,err,"",'--x', l="Diff")
    plt.title("Sinusoide : $f_e=$" + str(fe) + ", $f =$ " + str(f) + ", $d =$ " + str(nT) )
    mse=MSE(y,z)
    var=variance(y)
    snr=SNR(var,mse)
    plt.title("Sinusoide: fe="+str(fe)+ ", f="+str(f)+", d="+ str(nT/50.0)+" MSE= "+str(mse)+" SNR= "+str(snr))
    plt.legend()
  
  
   # print binaire
    #plt.show()
    print "MSE:"+str(mse)
    var=variance(y)
    print "Variance:"+str(var)
    rapport= SNR(var,mse) 
    print "SNR: "+str(var/mse)+" en db: "+str(rapport)
    print "step:"+str(step)
    print y
    print z
    entier=[]
    binaire=[]
    
    for i in range (len(z)):
       
        if(z[i]>=0):
            entier.append(int(math.floor(z[i]/step)))
            
        else:
            entier.append(int(math.floor(z[i]/step)))
    for i in range (len(entier)):
        binaire.append(Denary2Binary(entier[i],b))
        
    print entier 
    print binaire
    print 
    plt.show()
