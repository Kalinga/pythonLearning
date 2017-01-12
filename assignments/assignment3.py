import math
from operator import itemgetter
import random
import string
from  project.styleformat import heading
import sys
import string

heading("Module 3 Assignments: 1")

def add(op1, op2):
    return  op1 + op2

def sub(op1, op2):
    return  op1 - op2

def mul(op1, op2):
    return  op1 * op2

def div(op1, op2):
    return op1/op2

def calc(op, op1, op2):
    qStr = "What is {0} {1} {2}".format(op1, dict[type], op2)

    userInput= input(qStr)
    result = 0
    if op in ('A','a'):
        result = add(op1, op2)
    elif op in ('S', 's'):
        result = sub(op1, op2)
    elif op in ('M', 'm'):
        result = mul(op1, op2)
    elif op in ('D', 'd'):
        result = div(op1, op2)
    else:
        print "Wrong Input for question type (multiplication:M, addition:A, subtraction:S, division:D"

    if userInput == result:
        print "That's right -- well done"
    else:
        print "Sorry! You were wrong this time!!"

#Accept the input from User
level = raw_input("Please Enter difficulty level 'Easy' | 'Med' | 'Diff':  \n")
if level not in ['Easy', 'Med', 'Diff', 'easy', 'med', 'diff']:
    level = raw_input("Please Enter the level correctly: 'Easy' or 'Med' or 'Diff':  \n")
if level not in ['Easy', 'Med', 'Diff', 'easy', 'med', 'diff']:
    print "Wrong Input Exiting now....Thank you!"
    sys.exit(1)

questionCount = int(input("Please give us the number of question you want to attempt:  \n"))
if not questionCount > 0:
    questionCount = int(input( "Please re-enter the number of question you want to attempt" \
          " (question count must be an integer greater than 0): \n"))
if not questionCount > 0:
    print "Wrong Input Exiting now....Thank you!"
    sys.exit(1)

type = raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D):  \n")
if type not in ('M', 'm', 'D', 'd', 'S', 's', 'A', 'a'):
    print "You must key in one of this ('M', 'm', 'D', 'd', 'S', 's', 'A', 'a')"
    print "Wrong Input Exiting now....Thank you!"
    sys.exit(1)

dict = {'D': 'divided', 'A': 'added', 'S': 'subtracted', 'M': 'multiplied',
        'd': 'divided', 'a': 'added', 's': 'subtracted', 'm': 'multiplied'}

#Business Logic for iteration and invocation of calculation functions
while questionCount > 0:
    count = 0

    if level == 'Easy':
        op1 = random.choice(xrange(1,10))
        op2 = random.choice(xrange(1,5))
        calc(type, op1, op2)
    elif level == 'Med':
        op1 = random.choice(xrange(10,30))
        op2 = random.choice(xrange(5,10))
        calc(type, op1, op2)
    else:
        op1 = random.choice(xrange(30, 100))
        op2 = random.choice(xrange(20, 30))

        calc(type, op1, op2)

    questionCount -=1
    count += 1

    if (count == 5):
        option = raw_input("Do you want to quit now?(yes/no) \n")
        if option.lower() == 'yes':
            print "Exiting now....Thank you!"
            exit(0)

heading("Module 3 Assignments: 2")
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

heading("Module 3 Assignments: 3")
def mysort():
    mylist = [["john", 1, "a"], ["larry", 0, "b"]]
    mylist.sort(cmp=lambda x,y: cmp(x[1], y[1]))
    print  mylist

mysort()

heading("Module 3 Assignments: 3")
def mysort_itemgetter():
    mylist = [["john", 1, "a"], ["larry", 0, "b"]]
    mylist = sorted(mylist, key=itemgetter(1))
    print mylist

mysort_itemgetter()
