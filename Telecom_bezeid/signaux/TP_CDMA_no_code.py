import numpy as np
import matplotlib.pyplot as plt
import math
from array import array
from filecmp import demo

a = np.array([[0, 1], [3, 3]], float)

utilisateur1 = np.array([1, 0 ,0, 1, 1, 0],int)
utilisateur2 = np.array([1, 1, 0, 1, 0, 0],int)

print 'User A information: ' ,  utilisateur1
print 'User B information: ' ,  utilisateur2

#1- Coder l'information binaire de source en code NRZ (1 -> 1 et 0 -> -1) pour utilisateur A et B

length_user1=len(utilisateur1)
length_user2=len(utilisateur2)

#CODE STARTS HERE
"""on initialise les valeurs des utilisateurs a 1 et -1"""

for i in range(length_user1):
	if(utilisateur1[i]==1):
		utilisateur1[i]=1
	else:
		utilisateur1[i]=-1
		
for i in range(length_user2):
	if(utilisateur2[i]==1):
		utilisateur2[i]=1
	else:
		utilisateur2[i]=-1


#CODE ENDS HERE

fc=1   #carrier frequency
eb=2   #energy per bit
tb=100   #time per bit of message sequence 

#2- Prenez 100 ?chantillons par pour utilisateur A et utilisateur B et tracez le signal de bande de base au format NRZ bipolaire.

# Utilisateur A

t=np.arange(0.01,tb*length_user1+0.01,0.01, dtype=float)  #Horloge : on multiplie la longueur du tableau par tb 

basebandsig1=np.array([],float)

#CODE STARTS HERE


""""creation de 100 echatillons pour chaque signal"""
for x in utilisateur1:
	for i in range(100):
		basebandsig1=np.append(basebandsig1,x)


#CODE ENDS HERE

"""plt.figure(1)
plt.plot(basebandsig1)
#plt.xlabel('-')
#plt.ylabel('-')
plt.title('le signal de bande de base au format NRZ bipolaire pour utilisateur A')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 100*length_user1, -1.5 , 1.5 ])
plt.grid(True)"""

basebandsig2=np.array([],float)

#CODE STARTS HERE
for x in utilisateur2:
	for i in range(100):
		basebandsig2=np.append(basebandsig2,x)

#CODE ENDS HERE

"""plt.figure(2)
plt.plot(basebandsig2)
#plt.xlabel('-')
#plt.ylabel('-')
plt.title('le signal de bande de base au format NRZ bipolaire pour utilisateur B')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 100*length_user2, -1.5 , 1.5 ])
plt.grid(True)"""


# 3. Utilisez le BPSK (binary phase shift keying) pour moduler le signal. Attention: le taux d'echantillonnage  de porteuse sinusoidale correspond a la frequence d'echantillonnage par bit (100 echantillons par transporteur).  Tracer le signal BPSK.

# Utilisateur A
bpskmod1=np.array([],float)

#CODE STARTS HERE
for i in range(len(basebandsig1)):
		
		bpskmod1=np.append(bpskmod1,basebandsig1[i]*eb*np.cos(2*np.pi*i/100))  #t c est l index i diviser par le nombre d echatillon

#CODE ENDS HERE

"""plt.figure(3)
plt.plot(bpskmod1)
# plt.xlabel('-')
# plt.ylabel('-')
plt.title('BPSK signal pour utilisateur A')
plt.axis([0, 100*length_user1, -2 , 2 ])
plt.grid(True)"""

#Utilisateur B

bpskmod2=np.array([],float)

#CODE STARTS HERE

for i in range(len(basebandsig2)):
		
		bpskmod2=np.append(bpskmod2,basebandsig2[i]*eb*np.cos(2*np.pi*i/100))  #t c est l index i diviser par le nombre d echatillon

#CODE ENDS HERE
		
"""plt.figure(4)
plt.plot(bpskmod2)
# plt.xlabel('-')
# plt.ylabel('-')
plt.title('BPSK signal pour utilisateur B')
plt.axis([0, 100*length_user2, -2 , 2 ])
plt.grid(True)

#plot fft of BPSK sequence
#Utilisateur A
plt.figure(5)

#CODE STARTS HERE
Y = np.abs(np.fft.fft(bpskmod1))

plt.plot(Y)
plt.axis([0, 100*length_user1, 0 , 350])
plt.grid(True)
#CODE ENDS HERE


plt.title('FFT de BPSK signal pour utilisateur A')

#Utilisateur B
plt.figure(6)
#CODE STARTS HERE

Y = np.abs(np.fft.fft(bpskmod2))

plt.plot(Y)
plt.axis([0, 100*length_user2, 0 , 350])
plt.grid(True)


#CODE ENDS HERE
plt.title('FFT de BPSK signal pour utilisateur B')
 
#plt.show()

"""
# 4- Trouver le PN pour l?utilisateur A et B.

# Utilisateur A
# Contenu initial de registres est 1010

Contenu_initial_A=np.array([1, -1, 1, -1],float);

pn1=np.array([],float)

#CODE STARTS HERE

for i in range(60):
	pn1=np.append(pn1, Contenu_initial_A[3])
	tmp=Contenu_initial_A[3]
	Contenu_initial_A[3]=Contenu_initial_A[2]
	Contenu_initial_A[2]=Contenu_initial_A[1]
	Contenu_initial_A[1]=Contenu_initial_A[0]
	Contenu_initial_A[0]=-(tmp*Contenu_initial_A[3])
	




#CODE ENDS HERE

print 'PIN for A is:', pn1.astype(int), len(pn1)

#PIN for A is: [-1  1 -1  1  1  1  1 -1 -1 -1  1 -1 -1  1  1 -1  1 -1  1  1  1  1 -1 -1 -1
 # 1 -1 -1  1  1 -1  1 -1  1  1  1  1 -1 -1 -1  1 -1 -1  1  1 -1  1 -1  1  1
 # 1  1 -1 -1 -1  1 -1 -1  1  1]


# Utilisateur B
# Contenu initial de registres est 0101

Contenu_initial_B=np.array([-1, 1, -1, 1],float);

pn2=np.array([],float)

#CODE STARTS HERE


for i in range(60):
	pn2=np.append(pn2, Contenu_initial_B[3])
	tmp=Contenu_initial_B[3]
	Contenu_initial_B[3]=Contenu_initial_B[2]
	Contenu_initial_B[2]=Contenu_initial_B[1]
	Contenu_initial_B[1]=Contenu_initial_B[0]
	Contenu_initial_B[0]=-(tmp*Contenu_initial_B[3])



#CODE ENDS HERE

print 'PIN for B is:', pn2.astype(int), len(pn2)

#PIN for B is: [ 1 -1  1 -1  1  1  1  1 -1 -1 -1  1 -1 -1  1  1 -1  1 -1  1  1  1  1 -1 -1
# -1  1 -1 -1  1  1 -1  1 -1  1  1  1  1 -1 -1 -1  1 -1 -1  1  1 -1  1 -1  1
#  1  1  1 -1 -1 -1  1 -1 -1  1]

"""
5. On fait XOR entre code PN et le signal base band (BB). 
Multiplier le signal BPSK module avec le signal (BB XOR PIN) et tracer le signal pour Utilisateur A et B.
(attention : no de chip par bit * no d'echantillons par chip = no d'echantillons par bit de BPSK signal module).""" 

#Utilisateur A
len_pn1=len(pn1)
pnupsampled1=np.array([],float)


 
#CODE STARTS HERE

for i in range(len_pn1):
	for j in range(10):
 		pnupsampled1=np.append(pnupsampled1,pn1[i])
#CODE ENDS HERE



sigtx1=np.array([],float)

#CODE STARTS HERE
for i in range(len(bpskmod1)):
	sigtx1=np.append(sigtx1,pnupsampled1[i]*bpskmod1[i])




#CODE ENDS HERE
"""
plt.figure(7)
plt.plot(sigtx1)
plt.axis([0, 100*length_user1, -2, 2]);
plt.title('Signal transmit pour utilisateur A')
"""
#Utilisateur B
len_pn2=len(pn2)
pnupsampled2=np.array([],float)

#CODE STARTS HERE
for i in range(len_pn2):
	for j in range(10):
 		pnupsampled2=np.append(pnupsampled2,pn2[i])

#CODE ENDS HERE



sigtx2=np.array([],float)

#CODE STARTS HERE
for i in range(len(bpskmod2)):
	sigtx2=np.append(sigtx2,pnupsampled2[i]*bpskmod2[i])


#CODE ENDS HERE
"""
plt.figure(8)
plt.plot(sigtx2)
plt.axis([0, 100*length_user2, -2, 2]);
plt.title('Signal transmit pour utilisateur B')

# plot fft of BPSK sequence
#Utilisateur A
plt.figure(9)
#CODE STARTS HERE

Y = np.abs(np.fft.fft(sigtx1))

plt.plot(Y)
plt.axis([0, len_pn1, 0 , 350])
plt.grid(True)

#CODE ENDS HERE
plt.title('FFT du signal transmit pour utilisateur A')

#Utilisateur B
plt.figure(10)
#CODE STARTS HERE

Y = np.abs(np.fft.fft(sigtx2))

plt.plot(Y)
plt.axis([0, len_pn2, 0, 350])
plt.grid(True)

#CODE ENDS HERE
plt.title('FFT du signal transmit pour utilisateur B')
	
"""

#%%%%%%%%%%%%%%% Le signal de utilisateur A est ajout? au signal du utilisateur B  %%%%%%%%%%%


#CODE STARTS HERE

composite_signal=sigtx1+sigtx2



#CODE ENDS HERE

#%%%%%%%%%%%%% AWGN CHANNEL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#composite_signal=awgn(composite_signal,snr_in_dbs);  %% SNR of % dbs
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# Demodulation Pour Utilisateur A

rx1=np.array([],float)
#CODE STARTS HERE


rx1=composite_signal*pnupsampled1

#CODE ENDS HERE

"""plt.figure(11)
plt.plot(rx1)
"""
# BPSK DEMODULATION pour utilisateur A
demodcar1=np.array([],float)

 		
 		
 		
#CODE STARTS HERE
for i in range(len(rx1)):
	demodcar1=np.append(demodcar1,eb*math.cos(2*math.pi*i/100))




#CODE ENDS HERE
    
bpskdemod1=np.array([],float)

#CODE STARTS HERE
bpskdemod1=rx1*demodcar1



#CODE ENDS HERE

plt.figure(12)
plt.plot(bpskdemod1)
plt.title('sourtie de bpsk demod pur utilisateur A ')

len_dmod1=len(bpskdemod1)
SUM=np.zeros((1,len_dmod1/100), dtype=float)

#CODE STARTS HERE
"""on parcourt tous les elements du tableau bpskdemod1 et on effectue la somme sur tous les 100 elements , 
	si la somme est positive on modifie la case i a 1 sinon on la mets a 0 ; a la sortie on affiche la tableau SUM.
	On verifie qu'on a bien le signal original"""

n=0
s=0
for i in range(6):
	s=0
	n+=100
	while(j<n):
		s+=bpskdemod1[j]
		j+=1
	if(s>0):
		SUM=np.append(SUM,1)
	else:
		SUM=np.append(SUM,0)
		
print(SUM)


#CODE ENDS HERE

rxbits1=np.array([],float)
#CODE STARTS HERE


#CODE ENDS HERE

#print 'Decoded user A information:' , rxbits1


# Demodulation Pour Utilisateur B

rx2=np.array([],float)
#CODE STARTS HERE
rx2=composite_signal*pnupsampled2


#CODE ENDS HERE
#plt.figure(13)
#plt.plot(rx2)

# BPSK DEMODULATION pour utilisateur B
demodcar2=np.array([],float)


#CODE STARTS HERE

for i in range(len(rx2)):
	demodcar2=np.append(demodcar2,eb*math.cos(2*math.pi*i/100))





#CODE ENDS HERE
    
bpskdemod2=np.array([],float)
    
#CODE STARTS HERE

bpskdemod2=rx2*demodcar2

#CODE ENDS HERE

plt.figure(14)
plt.plot(bpskdemod2)
plt.title('sourtie de bpsk demod pur utilisateur B ')

len_dmod2=len(bpskdemod2)
SUM=np.zeros((1,len_dmod2/100), dtype=float)

#CODE STARTS HERE
"""on parcourt tous les elements du tableau bpskdemod2 et on effectue la somme sur tous les 100 elements , 
	si la somme est positive on modifie la case i a 1 sinon on la mets a 0 ; a la sortie on affiche la tableau SUM.
	On verifie qu'on a bien le signal original"""
n=0
s=0
j=0
for i in range(6):
	s=0
	n+=100
	while(j<n):
		s+=bpskdemod2[j]
		j+=1
	if(s>0):
		SUM[i]=np.e(SUM,1)
	else:
		SUM=np.append(SUM,0)
		
print(SUM)
#CODE ENDS HERE

rxbits2=np.array([],float)
#CODE STARTS HERE



#CODE ENDS HERE

print 'Decoded user B information:' , rxbits2


plt.show()
