#!/usr/bin/python
# coding=UTF-8
import numpy as np
import random as rn
import scipy as sp

from  testmodule.styleformat import heading

heading("Module 6 Assignments: 1 [Cartesan and Polar co-ordinates]")
def cartesan_to_polar(one_darray):
    print one_darray
    x = one_darray[0]
    y = one_darray[1]
    r = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan(float(y) / float(x))
    print "r {0} theta{1}".format(str(r), str (theta))
    #return [r, theta]

rows, col = 10, 2
print "a random 10 x 2 matrix representing Cartesian coordinates"
co_ordinates = np.array([[rn.randint(1, 100) for x in range(2)] for y in range(rows)], dtype=np.float)
print co_ordinates
print co_ordinates.shape
polar_cordinates = co_ordinates.copy()
con = lambda x, y: [np.sqrt(x ** 2 + y ** 2), np.arctan(float(y) / float(x))]
for i in range(10):
    cartesan_to_polar(polar_cordinates[i, :])
    polar_cordinates[i] =con(polar_cordinates[i,0], polar_cordinates[i,1])
print "~" * 10 + "Converted polar_cordinates" + "~" * 10
print polar_cordinates

heading("Module 6 Assignments: 2 Python Vector")
# Create random vector of size 50 and replace the maximum value by 0 and minimum value by 100.
Vector = np.array([rn.randint(0,60) for x in range(50)])
print Vector
min_max = np.array(Vector.argsort()[[0, -1]])
print min_max
Vector[min_max[0]] = 100
Vector[min_max[1]] = 0
print Vector

heading("Module 6 Assignments: 3 matrix using scipy")
ten_ten_matrix = sp.eye(10, dtype=np.float) * 2
print ten_ten_matrix
#ten_ten_matrix * 2
#sp.multiply(ten_ten_matrix, [2])
print ten_ten_matrix