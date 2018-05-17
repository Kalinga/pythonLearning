import string

from  testmodule.styleformat import heading

heading("Module 2 Assignments: 5")
a = [4,7,3,2,5,9]

for index, value in enumerate(a):
    print "index: " + str(index) + str(", ") + "value: " + str(value)
for item in a:
    print(str(item) + " is at position " + str(a.index(item) + 1))

heading("Module 2 Assignments: 6")
upper = list(string.uppercase)
dictUpper = dict(enumerate(upper))
revUpperDict = dict((y,x + 1) for x,y in dictUpper.iteritems())
print revUpperDict

theDict = {chr(y):y - 64 for y in range(65, 91)}
print theDict

heading("Module 2 Assignments: 7")
dict1 = { 'a': 1, 'b':2 }
dictRev = dict((y,x) for x,y  in dict1.items())
print  dictRev

heading("Module 2 Assignments: 8")
L = ['a', 'b', 'c', 'd']
dictRes = dict((y,x + 1) for x,y in enumerate(L))
print dictRes