'''
Created on 4 fevr. 2014

@author: yezide
'''
import math
import matplotlib.pyplot as plt
#from scipy.signal.wavefroms import sawtooth, square
import numpy as np
import pylab as pl
from math import floor
from _ast import Str
from matplotlib.backends import pylab_setup

class signal:   
    
    def __init__(self,a,ph,f,fe,nT,title,format):
        self.a=a
        self.ph=ph
        self.f=f
        self.fe=fe
        self.nT=nT
        self.omega = 2*math.pi*f
        self.N = (self.fe/self.f)
        self.te = 1.0/self.fe
        self.T=1.0/self.f
        self.k=self.f+1   
        self.title=title
        self.format=format 
        self.kmax=20
       # self.mult_freq=1
    """cette fonction permet de renvoyer deux liste : une qui represente le temps par seconde l'autre le voltage"""
    def make(self):
        sig_t = []
        sig_s = []
        for i in range(self.N*self.nT):
            t = self.te*i
            sig_t.append(t)
            sig_s.append(self.get_volte(t))
           
        return sig_t, sig_s
    
    def fourier(self):
        sig_an=[]
        sig_bn=[]
        i=0
        while(i< self.kmax):    
            sig_an.append(self.an(i))
            sig_bn.append(self.bn(i))
            i=i+1
        
        sig_t = []
        sig_s = []
        sig_a = []
        sig_b=[]
        for i in range(int(self.N*4)):
            t = self.te*i
            sig_t.append(t)
            k=0
            tmp=0.0
            while k < self.kmax:
                tmp+=sig_an[k] * math.cos(2*math.pi*k*self.f*t) + (sig_bn[k]*math.sin(2*math.pi*k*self.f*t))
                
                
                k=k+1
            sig_s.append(tmp)
        sig_n=[]
        i=0
        while(i<=self.kmax):
            sig_n.append(0)
            sig_a.append(self.an(i))
            sig_b.append(self.bn(i))
            
            i+=1
            
        return sig_t,sig_s,sig_a,sig_b,sig_n
    
    def plot(self,inx, iny, label_y, format):
        plt.plot(inx,iny,format)
        #plt.xlabel('time (s)')
        plt.ylabel(label_y)
        #plt.title("Signel synthesis and Coess")
        #plt.ylim([-1.5, 1.5])
        plt.grid(True)
    
    
    def verifie_length(self, t, label, format):
        t1=[]
        i=0
        while(i<=self.kmax):
            t1.append(i)
            i+=1
        self.plot(t1, t[:len(t1)],label,format)
        
    def fft(self): 
        f1 = self.fe * 0.01
        f2 = self.fe * 0.02
        f3 = self.fe * 0.4
        N = 128
        Fs=self.fe
        N=self.N
        Ts = 1./Fs      # the sampling period
        freqStep = Fs/N  # resolution of the frequency IN FREQUENCY DOMAIN
        mult=self.mult_freq()
        f = mult*freqStep   # frequency of the sine wave : On choisit un multiple de freqstep
        T = 1.0/f    # periode de la sinusoide
        
        print "Signal de %d points dans le domaine frequentiel : periode frequentielle = %f Hz" %(N,freqStep)
        print "Signal de %d points dans le domaine du temps : frequence : %f Hz, periode temporelle : %f s\n" %(N,f,T) 
     
        t = np.arange(N)*Ts         # N ticks in time domain, t = n*Ts
        y=[]
        for i in range(len(t)):
            y.append(self.get_volte_fft(t[i],T))
       
        # Calcul du spectre du signal y 
        Y = np.fft.fft(y)           # Spectrum
        print "fft result is a ", type(Y) ,"[", len(Y) ,"]", ' of ', type(Y[0]), "\n"
        print Y 
       
        Y = np.fft.fftshift(Y)      # middles the zero-point's axis
        Y = Y/N                     # Normalization
    
        # Plot
        pl.figure(figsize=(8,8))
        pl.subplots_adjust(hspace=.4)
        # Plot time data ---------------------------------------
        pl.subplot(3,1,1)
        pl.plot(t, y, '.-')
        pl.grid("on")
        pl.xlabel('Time (seconds)')
        pl.ylabel('Amplitude')
        pl.title(self.title)
        pl.axis('tight')
        freq = freqStep * np.arange(-N/2, N/2)  # ticks in frequency domain   
        # Plot spectral magnitude ------------------------------
        pl.subplot(3,1,2)
        pl.plot(freq, abs(Y), '.-g')
        pl.grid("on")
        pl.xlabel('Frequency')
        pl.ylabel('Magnitude (Linear)')   
        # Plot phase -------------------------------------------
        pl.subplot(3,1,3)
        pl.plot(freq, np.angle(Y), '.-g')
        pl.grid("on")
        pl.xlabel('Frequency')
        pl.ylabel('Phase (Radian)')
        pl.show()

        return Fs,N,Ts,freqStep,f,T,t,y
    
    """peremet de tracer un graphe en appliquant la fonction plot"""
    def dessiner(self):
        x,y,z,w,u=self.fourier()
        plt.subplot(311)
        self.plot(x, y, "s(k*Te)", "-bo")
        plt.subplot(312)
        self.verifie_length(z, "an de S(nF0)", 'go')
        plt.subplot(313)
        self.verifie_length(w, "bn de S(nF0)", "ro")
    def signe(self,sig):
        if(sig>0):
            return 1
        elif(sig<0):
            return-1
        else:
            return 0   
        
        
        
    


 
class carre(signal):
    """cette fonction permet de renvoyer le voltage du signal carre"""
    def get_volte(self,t):
        
        if(self.a*math.sin((self.omega*t)+self.ph)>0):
            return self.a
        elif(self.a*math.sin((self.omega*t)+self.ph)<0):
            return -self.a
        else:
            return 0
      
    
    def get_volte_fft(self,t,T):
         if(self.a*math.cos(self.mult_freq()*self.omega*t)>0):
             return -self.a
         elif(self.a*math.cos(self.mult_freq()*self.omega)<0):
             return self.a
         else:
             return 0
        
    """renvoie le multiple de la frequence"""
    def mult_freq(self):
        return 3
    
    def an(self,k):
        return 0
    
    def bn(self,k):
        
        if(k%2==0):
            return 0
        else:
            return ((4*self.a)/(math.pi*k))

class sinusoide(signal):
    """cette fonction permet de renvoyer le voltage du signal sinusoidale"""
    def get_volte(self,t):
        return self.a*math.sin((self.omega*t)+self.ph)
    
    def get_volte_fft(self,t,T):
         return self.a*math.cos(self.mult_freq()*self.omega*t)
    
    """renvoie le multiple de la frequence"""
    def mult_freq(self):
           return 3
       
       
       


class multi_sinusoides(signal):
        
        
    
    
        def filtrer_signal(self):
            
            fe = 3000
            f1 = fe * 0.01
            f2 = fe * 0.02
            f3 = fe * 0.4
            N = 128
            
            a = 0.5
            Fs = fe
            Ts = 1./Fs
            freqStep = (Fs * 1.0)/N
            f = 3*freqStep
            T = 1.0/f
           # print "Signal de %d points dans le domaine frequentiel : periode frequentielle = %f Hz" %(N, freqStep)
           # print "Signal de %d points dans le domaine du temps : frequence : %f Hz , periode temporelle : %f s\n" %(N , f , T )
            
            #Utilisation de la vectoristation de numpy !!
            sig_t = np.arange(0,N*(1.0/fe),1.0/fe)
            t = sig_t
            sig_all = (np.cos (2*math.pi*f1* sig_t ) + np.cos (2* math.pi*f2* sig_t )+ np.cos (2* math.pi*f3* sig_t ))/3.0
            y =sig_all
         
            b = [-6.849167e-003, 1.949014e-003, 1.309874e-002,1.100677e-002,
            -6.661435e-003,-1.321869e-002, 6.819504e-003, 2.292400e-002,7.732160e-004,
            -3.153488e-002,-1.384843e-002,4.054618e-002,3.841148e-002,-4.790497e-002,
            -8.973017e-002, 5.285565e-002,3.126515e-001, 4.454146e-001,3.126515e-001,
            5.285565e-002,-8.973017e-002,-4.790497e-002, 3.841148e-002, 4.054618e-002,
            -1.384843e-002,-3.153488e-002, 7.732160e-004,2.292400e-002,6.819504e-003,
            -1.321869e-002,-6.661435e-003, 1.100677e-002,1.309874e-002,1.949014e-003,
            -6.849167e-003
            ]
            filter = np.zeros(128)
            for i  in range(len(sig_all)):
                n=0
                while(n<35):
                    if((i-n)<0):
                        sig=0
                    else:
                        sig=(sig_all[i-n])
                    filter[i]=filter[i]+(b[n]*sig)
                    n=n+1 
            y=filter
         
            Y = np.fft.fft(y)
           # print "fft result is a ", type(Y), "[", len(Y), "]", ' of ', type(Y[0]), "\n"
           # print Y
            
            Y = np.fft.fftshift(Y)
            Y = Y/N
            
            #Plot
            pl.figure(figsize=(8,8))
            pl.subplots_adjust(hspace = 0.4)
            
            #plot time data
            pl.subplot(3,1,1)
            pl.plot(t*8000,y,'.-r')
            pl.grid("on")
            pl.xlabel('Time (seconds)')
            pl.ylabel('Amplitude')
            pl.title('Sinusoidale signals')
            pl.axis('tight')
            freq = freqStep * np.arange(-N/2,N/2)
            
            #plot spectral magnitude
            pl.subplot(3,1,2)
            pl.plot(freq, abs(Y), '.-b')
            pl.grid("on")
            pl.xlabel('Frequency')
            pl.ylabel('Magnitude (linear)')
            
            #plot phase
            pl.subplot(3,1,3)
            pl.plot(freq, np.angle(Y), '.-b')
            pl.grid("on")
            pl.xlabel('Frequency')
            pl.ylabel('Phase (radian)')
            
            pl.show()

        
        
            """renvoie le multiple de la frequence"""
            def mult_freq(self):
                return 3
    
    
        def sig_composite(self):
            f1 = self.fe * 0.01
            f2 = self.fe * 0.02
            f3 = self.fe * 0.4
            N = self.N
            Fs = self.fe
            Ts = 1./Fs
            freqStep = (Fs * 1.0)/N
            f = 3*freqStep
            T = 1.0/f
            
            print "Signal de %d points dans le domaine frequentiel : periode frequentielle = %f Hz" %(N, freqStep)
            print "Signal de %d points dans le domaine du temps : frequence : %f Hz , periode temporelle : %f s\n" %(N , f , T )
        
            #Utilisation de la vectoristation de numpy !!
            sig_t = np.arange(0,N*(1.0/self.fe),1.0/self.fe)
            t = sig_t
            y=(np.cos(2*math.pi*f1* sig_t ) + np.cos (2* math.pi*f2* sig_t ) + np.cos (2* math.pi*f3* sig_t ))/3.0
            #sig_all = (np.cos (2*math.pi*f1* sig_t ) + np.cos (2* math.pi*f2* sig_t )+ np.cos (2* math.pi*f3* sig_t ))/3.0
            
            
            #Calcul du spectre du signal y
            Y = np.fft.fft(y)
            print "fft result is a ", type(Y), "[", len(Y), "]", ' of ', type(Y[0]), "\n"
            print Y
            
            Y = np.fft.fftshift(Y)
            Y = Y/N
            
            #Plot
            pl.figure(figsize=(8,8))
            pl.subplots_adjust(hspace = 0.4)
            
            #plot time data
            pl.subplot(3,1,1)
            pl.plot(t*8000,y,'.-r')
            pl.grid("on")
            pl.xlabel('Time (seconds)')
            pl.ylabel('Amplitude')
            pl.title('Sinusoidale signals')
            pl.axis('tight')
            freq = freqStep * np.arange(-N/2,N/2)
            
            #plot spectral magnitude
            pl.subplot(3,1,2)
            pl.plot(freq, abs(Y), '.-b')
            pl.grid("on")
            pl.xlabel('Frequency')
            pl.ylabel('Magnitude (linear)')
            
            #plot phase
            pl.subplot(3,1,3)
            pl.plot(freq, np.angle(Y), '.-b')
            pl.grid("on")
            pl.xlabel('Frequency')
            pl.ylabel('Phase (radian)')
            pl.show()
            
        
    

        
        
class denDeScie(signal):
    """cette fonction permet de renvoyer le voltage du signal denDeScie""" 
    def get_volte(self,t):
        return 2*self.a*((t/self.T)-math.floor(t/self.T)-0.5)
    
    def an(self,k):
        return 0
    
    def bn(self,k):
        if(k==0):
            return 0
        else:
            return ((-2*self.a)/(math.pi*k))
        
    def get_volte_fft(self,t,T):
        
        return 2*self.a*((t/T)-math.floor(t/T)-0.5)
    
    """renvoie le multiple de la frequence"""
    def mult_freq(self):
        return 4.27    
    
class triangle(signal):
    """cette fonction permet de renvoyer le voltage du signal triangle"""   
    def get_volte(self,t):
        return self.a*(4* abs((t/self.T) - math.floor((t/self.T)+0.5))-1.0)
    
    def get_volte_fft(self,t,T):
        return self.a*(4* abs((t/T) - math.floor((t/T)+0.5))-1.0)
    
    """renvoie le multiple de la frequence"""
    def mult_freq(self):
        return 3   
    
    def an(self,k):
        if(k%2==0):
            return 0
        else:
            return ((8*self.a)/(math.pow(math.pi*k,2)))
    
    def bn(self,k):
        return 0
     
if __name__ == '__main__':
   
    plt.subplots_adjust(wspace=0.5)
    

    tr=triangle(1.5,0,100.0,3000.0,0,"", "")
    d=denDeScie(1.5,0,100.0,3000.0,0,"", "")
    c=carre(1,0,100.0,3000.0,1,"", "")
    c.dessiner()
    plt.show()
   


        