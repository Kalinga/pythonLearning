import operator
import re

def sumall(*args):
    result = lambda *args:sum(*args)
    print type(result)
    print result(*args)

l = [1,2,345,5]
sumall(l)


def doubleTheValue(list):
    modList = map(lambda x:x*2, list)
    print modList

l = [1,23,34,45,456,56,4]
doubleTheValue(l)

def evenValue(list):
    mapList = map(lambda x:x%2 !=0, list)
    print mapList
    filteredList = filter(lambda x: x % 2 != 0, list)
    print filteredList

l = [1,23,34,54,4,5,4]
evenValue(l)
t = (1,23,34,54,4,5,4)
evenValue(t)

#Using getKey
def sort(li):
    def getKey(li):
        return  li[1]

    sortedList = sorted(li, key = getKey)
    print "\nUsing a user defined function for the 'key':"
    print sortedList

l = [[23,345], [20,345], [234,23], [23,234],[23,34],[45,367], [32, 345]]
sort(l)

print "\nUsing a lambda (x[1]) function for the 'key':"
print sorted(l, key=lambda x:x[1])

print "\nUsing a lambda (x[1], -x[0]) function for the 'key':"
print sorted(l, key=lambda x:(x[1], -x[0]))

print "\nUsing operator.itemgetter(1) for the 'key':"
print sorted(l, key=operator.itemgetter(1))

print "\nUsing operator.itemgetter(1,0) for the 'key':"
print sorted(l, key=operator.itemgetter(1,0))

print "\nUsing operator.itemgetter(1,0) for the 'key': IS MORE OPTIMISED"

arr = ["date_2015-1-1", "date_2015-1-10", "date_2015-1-2"]

def sort_key(_str):
    return [ int(s) if s.isdigit() else s for s in re.split(r'(\d+)', _str) ]

arr = ["date_2015-1-1", "date_2015-1-10", "date_2015-1-2"]
print "\nSorting using a regex"
print arr
print sorted(arr, key=sort_key)

DATA = [
    ('Jones', 'Jane', 58),
    ('Smith', 'Anne', 30),
    ('Jones', 'Fred', 30),
    ('Smith', 'John', 60),
    ('Smith', 'Fred', 30),
    ('Jones', 'Anne', 30),
    ('Smith', 'Jane', 58),
    ('Smith', 'Twin2', 3),
    ('Jones', 'John', 60),
    ('Smith', 'Twin1', 3),
    ('Jones', 'Twin1', 3),
    ('Jones', 'Twin2', 3)
]

print "\nRaw Data of Surname, Age, Firstname:"
for item in DATA:
    print item
print "\nSort by Surname, Age, Firstname:"
for item in sorted(DATA, key=lambda item:(item[0], item[2], item[1])):
    print item
print "\nSort by Surname, Age DESCENDING, Firstname:"
for item in sorted(DATA, key=lambda item:(item[0], -item[2], item[1])):
    print item