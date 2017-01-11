import math
from operator import itemgetter
#Write a recursive function to compute x raised to the power of n.
def power(x, y):
    if x == 0:
        return float('nan')
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
print power(0,0)
print power(0,1)
print power(1,0)
print power(1,1)
print power(1,10)
print power(10,1)
print power(2,10)

def mysort():
    mylist = [["john", 1, "a"], ["larry", 0, "b"]]
    mylist.sort(cmp=lambda x,y: cmp(x[1], y[1]))
    print  mylist

mysort()

def mysort_itemgetter():
    mylist = [["john", 1, "a"], ["larry", 0, "b"]]
    mylist = sorted(mylist, key=itemgetter(1))
    print mylist

mysort_itemgetter()