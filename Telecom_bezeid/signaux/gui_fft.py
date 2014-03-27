#!/usr/bin/env python
"""
http://yukuan.blogspot.com/2006/12/fft-in-python.html
This example demonstrates the FFT of a simple sine wave and displays its
bilateral spectrum.  Since the frequency of the sine wave is folded by
whole number freqStep, the bilateral spectrum will display two non-zero point.
 
Note:
 
This example is coded original in Matlab from Roger Jang's
Audio Signal Processing page.  I translated it into Python with matplotlib.
 
See Also:
 
- "Discrete Fourier Transform" by Roger Jang
    <http://140.114.76.148/jang/books/audioSignalProcessing/ftDiscrete.asp>
"""

from signaux.tp1_usingclasses import signal, denDeScie, sinusoide,\
    carre, triangle, multi_sinusoides
from sympy.polys.groebnertools import sig_cmp



if __name__ == '__main__':
     d=denDeScie(1, 1, 23.5, 3000, 1, "signal denDescie", "")
     s=sinusoide(1, 0, 250, 8000, 1, "signal sinusoidal", "")
     c=carre(1, 0, 25, 3000, 1, "signal carre", "")
     t=triangle(1, 0, 23.5, 3000, 1, "signal triangle", "")
     ss=multi_sinusoides(1, 0, 23.5, 3000, 1, "signal sinusoidal", "")
     ##ss.sig_composite()
     ss.filtrer_signal()

""""d.fft()
     c.fft()
     t.fft()"""