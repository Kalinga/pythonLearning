import scipy as sp
from scipy import stats
from scipy import constants
from scipy import integrate

import math

import numpy

randoms = sp.randn(100)
print randoms
print "mean: " + str(sp.mean(randoms))
print sp.stats.describe(randoms)
n, min_max, mean, var, skew, kurt = stats.describe(randoms)
print n
print  min_max
print mean
print var
print skew
print kurt
print '*' * 10 + 'constants'+'*' * 10
for const in constants.physical_constants:
    print const

print '*' * 10 + 'Integration'+'*' * 10
print integrate.quad(lambda x : math.exp(-x*x), -sp.inf, sp.inf)

print '*' * 10 + 'Linear algebric equation with 3 variables'+'*' * 10
#4x + y -2z = 0
#2x - 3y +3z = 9
#-6x -2y +z = 0
A = numpy.mat('[4 1 -2; 2 -3 3; -6 -2 1]')
B = numpy.mat('[0; 9; 0]')
print A.I * B
print sp.linalg.solve(A, B)