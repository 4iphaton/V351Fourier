import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

U, v = np.genfromtxt('../../content/values/b_saege.txt',unpack=True)
U0 = 800/2
v0 = 69440

# koeffizienten
k1 = (U0*2)/(const.pi* 1)
print( "koeff 1", k1)
k3 = (U0*2)/(const.pi* 2)
print( "koeff 2", k3)
k5 = (U0*2)/(const.pi* 3)
print( "koeff 3", k5)
k7 = (U0*2)/(const.pi* 4)
print( "koeff 4", k7)
k9 = (U0*2)/(const.pi* 5)
print( "koeff 5", k9)
k11 = (U0*2)/(const.pi* 6)
print( "koeff 6", k11)
k13 = (U0*2)/(const.pi* 7)
print( "koeff 7", k13)
k15 = (U0*2)/(const.pi* 8)
print( "koeff 8", k15)
k17 = (U0*2)/(const.pi* 9)
print( "koeff 9", k17)

#abweichung
a1 = 100*(k1-U[0])/k1
print("abw 1", a1 )
a3 = 100*(k3-U[1])/k3
print("abw 2", a3 )
a5 = 100*(k5-U[2])/k5
print("abw 3", a5 )

a7 = 100*(k7-U[3])/k7
print("abw 4", a7 )
a9 = 100*(k9-U[4])/k9
print("abw 5", a9 )
a11 = 100*(k11-U[5])/k11
print("abw 6", a11 )
a13 = 100*(k13-U[6])/k13
print("abw 7", a13 )
a15 = 100*(k15-U[7])/k15
print("abw 8", a15 )
a17 = 100*(k17-U[8])/k17
print("abw 9", a17 )
