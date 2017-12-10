import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

U, v = np.genfromtxt('../../content/values/b_rechteck.txt',unpack=True)
k = 0
for x in U:
    k = 4/(const.pi*(x + 1))
    print(k)
    print((k-U[x])/k)
