__creator__='Kalinga'

import string
import sys

from  testmodule.styleformat import heading

#1. Write a program to print the:
#a. Number of lowercase 'a' and "o" in the following sentence.
#Discover, Learning, with, MySimpleClass

def firstTaskLowercaseCount():
    print "Calling " + firstTaskLowercaseCount.__name__

    str = "Discover, Learning, with, TeachMe"
    print "Number of 'a': %d, 'o': %d are there" % (str.count('a'), str.count('o'))

#b. Number of uppercase 'L' and 'N' in the following sentence.
def firstTaskUppercaseCount():
    print "\nCalling " + firstTaskUppercaseCount.__name__

    str = "Discover, Learning, with, TeachMe"
    print "Number of 'L': %d, 'N': %d are there" % (str.count('L'), str.count('N'))

#2. Write a program to remove the following from:
#www.edureka.in
#a. Remove all w' s before and after .edureka.
#b. Remove all lowercase letter before and after .edureka.

def secondTask_a():
    print "\nCalling " + secondTask_a.__name__
    str = "www.edureka.in"

    print str.strip('w')
    print sys.argv

def secondTask_b():
    print "\nCalling " + secondTask_b.__name__
    print "strip() works in removing from leading and trailing end not through out the text"
    str = "WWW.http.edureka.IN"
    newStr=''
    index = str.find(".edureka.")
    print index
    for i in range(index):
        #print i
        if (not str[i].islower()):
            newStr = newStr + str[i]

    print newStr
    newStr = newStr + ".edureka."
    for i in range(str.find(newStr) + len(newStr), len(str)):
        #print i
        if (not str[i].islower()):
            newStr = newStr + str[i]

    str = newStr
    print str

#c. Remove all printable characters
def secondTask_c():
    print "\nCalling " + secondTask_c.__name__
    str = "www.edureka.in"
    newStr = ''
    for i in range(len(str)):
        #print i
        if (not str[i] in string.printable):
            newStr = newStr + str[i]

    str = newStr
    print str


#3. Identify the type of numbers:

#a. 0X7AE
def thirdTask_a():
    print (type(0X7AE))

#b. 3+4j
def thirdTask_b():
    print (type(3+4j))

#c. -01234
def thirdTask_c():
    print (type(-01234))

#d. 3.14e-2
def thirdTask_d():
    print (type(3.14e-2))

#4. Write a program for String Formatting Operator % which should include the following conversions:

#a. Character
def fourthTask_a():
    option = "Y"
    print "\nInput option '%c' for Yes" %(option)

#b. Signed decimal integer
def fourthTask_b():
    print "Input integer '%i' with sign" % (-456)

#c. Octal integer
def fourthTask_c():
    print "Input number '%o' is Octal" % (0345)

#d. Hexadecimal integer (UPPERcase letters)
def fourthTask_d():
    print "Input number '%X' is HEX" % (0X12AF5)

#e. Floating point real number
def fourthTask_e():
    print "Input number '%f' is a Floating point Real number" % (234.34)

#f. Exponential notation (with lowercase 'e')
def fourthTask_f():
    print "Input number '%e' is a Floating point Real number" % (233454.34)

if __name__ =='__main__':

    heading("Module 1 Assignments: 1")

    firstTaskLowercaseCount()
    firstTaskUppercaseCount()

    heading("Module 1 Assignments: 2")

    secondTask_a()
    secondTask_b()
    secondTask_c()

    heading("Module 1 Assignments: 3")

    thirdTask_a()
    thirdTask_b()
    thirdTask_c()
    thirdTask_d()

    heading("Module 1 Assignments: 4")

    fourthTask_a()
    fourthTask_b()
    fourthTask_c()
    fourthTask_d()
    fourthTask_e()
    fourthTask_f()
