import random

#from  project.styleformat import heading

import sys
import string

#heading("Module 3 Assignments: 1")

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
level = raw_input("Please Enter difficulty level 'Easy' | 'Med' | 'Diff'")
if level not in ['Easy' , 'Med' , 'Diff']:
    level = raw_input("Please Enter the level correctly: 'Easy' or 'Med' or 'Diff'")
if level not in ['Easy' , 'Med' , 'Diff']:
    sys.exit(1)

questionCount = (int)(input("Please give us the number of question you want to attempt:"))
type = raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D)")
dict = {'D': 'divided', 'A': 'added', 'S': 'subtracted', 'M': 'multiplied',
        'd': 'divided', 'a': 'added', 's': 'subtracted', 'm': 'multiplied'}

#Business Logic for iteration and invocation of calculation functions
while questionCount > 0:
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
