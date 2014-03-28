'''
Created on 28 mars 2014

@author: yezide
'''
from numpy import sqrt, ones
from numpy.random import rand, randn
from time import time
 
N = 5000000
N0 = 1.0
 
# Begin
t = time()
 
x = 2 * (rand(N) >= 0.5) - 1
 
y = x + sqrt(N0/2) * randn(N)
 
y_d = 2 * (y >= 0) - 1
# End
print time() - t, "seconds"
 
errors = (x != y_d).sum()
print errors, "error bits"
print "Error probability:", 1.0 * errors / N