import random as rn

import string

print "randrange(1,10):"
for i in range(10):
    print rn.randrange(1,10)

print "rn.randint(1, 10)"
for i in range(10):
    print rn.randint(1, 10)

operations = ['Add', 'Sub', 'Mul', 'Div']
print "rn.choice(operations):"
for i in range(10):
    print rn.choice(operations)

#Random Password
passwd = ''.join(rn.choice(rn.choice(string.ascii_letters + string.digits)) for x in range(50))
print "Generated Random Passwd: ", passwd

gen = lambda x: ''.join(rn.choice(rn.choice(string.ascii_letters + string.digits)) for y in range(x))
print "10 Letter random passwd: ", gen(10)
