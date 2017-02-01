import numpy as np

arr = np.array([1,2,3])
print arr
arr = np.array(range(20))
print type(arr)
print arr.ndim
print arr.shape
print arr
print '*' * 30
arr1 = np.array([range(5,10),range(5)])
print type(arr1)
print "arr1.ndim: " + str(arr1.ndim)
print arr1.shape
print arr1.dtype
print arr1.itemsize
print arr1
print arr1.data
print '*' * 30
print arr1[0]
print arr1[1]
print arr1[0,0]
print arr1[0,1]
print arr1[1,0]
print arr1[:,1:3]
print arr1[:,0:0]
print '*' * 30
zeros = np.zeros(2)
print zeros
zeros_dd = np.zeros([2,5])
print zeros_dd
print type(zeros_dd[0,0])
print zeros.dtype
print '3'+'*' * 30
arr2 = np.array(range(10), dtype=np.int)
print arr2
ones = np.ones([100,100], dtype=np.int)
print ones
l1 = [1,2,3,4,5]
l2 = map(lambda x:x*2, l1)
print l1 + l2
al1 = np.array(l1)
al2 = np.array(l2)
print al1 + al2
print '*' * 10 + 'Shallow Copy & Deep Copy'+'*' * 10
evens = np.arange(0,21,2)
print evens
sevens = evens.view()
print sevens
sevens[10] = 200
print evens
print sevens
devens = evens.copy()
devens[10] = 2000
evens[10] = 20
print evens
print devens
print '*' * 10 + 'mean sum min max'+'*' * 10
print evens.mean()
print evens.sum()
print evens.min()
print  evens.max()
print evens.nonzero()
print '*' * 10 + 'sort and argsort'+'*' * 10
unsorted = [5,45,521,-2,-25,0,325]
unsorted_arr = np.array(unsorted, dtype=np.int8)
print np.sort(unsorted_arr)
print np.argsort(unsorted_arr)
print unsorted_arr[np.argsort(unsorted_arr)]
print '*' * 10 + 'transpose, invert and eye'+'*' * 10
print arr1
print arr1.transpose()
print np.invert(arr1)
print arr1
print np.eye(3, dtype=np.int8)
print '*' * 10 + 'Vectorizing Function'+'*' * 10
vsinc = np.vectorize(np.sinc)
print vsinc([1.3, 1.5])
print np.sinc([1.3, 1.5])

