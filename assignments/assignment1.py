__creator__='Kalinga'

#1. Write a program to print the:
#a. Number of lowercase 'a' and "o" in the following sentence.
#Discover, Learning, with, Edureka

def firstTaskLowercaseCount():
    print "Calling " + firstTaskLowercaseCount.__name__
    lowCount = 0
    str = "Discover, Learning, with, Edureka"
    for letter in str:
        if letter.islower():
            lowCount +=1
    print lowCount
    print "Number of small letters are there"


def firstTaskUppercaseCount():
    print "\nCalling " + firstTaskUppercaseCount.__name__
    uppCount = 0
    for letter in "Discover, Learning, with, Edureka":
        if letter.isupper():
            uppCount =uppCount + 1
    print "%s Number of Upper Case letters are there" %uppCount


#2. Write a program to remove the following from:
#www.edureka.in
#a. Remove all w' s before and after .edureka.
#b. Remove all lowercase letter before and after .edureka.
#c. Remove all printable characters
def secondTask_a():
    print "\nCalling " + secondTask_a.__name__
    str = "www.edureka.in"
    index = str.find(".edureka.")


def secondTask_b():
    pass
def secondTask_c():
    pass

#3. Identify the type of numbers:
#a. 0X7AE
#b. 3+4j
#c. -01234
#d. 3.14e-2
def thirdTask_a():
    pass
def thirdTask_b():
    pass
def thirdTask_c():
    pass
def thirdTask_d():
    pass

#4. Write a program for String Formatting Operator % which should include the following conversions:
#a. Character
#b. Signed decimal integer
#c. Octal integer
#d. Hexadecimal integer (UPPERcase letters)
#e. Floating point real number
#f. Exponential notation (with lowercase 'e')
def fourthTask_a():
    pass
def fourthTask_b():
    pass
def fourthTask_c():
    pass
def fourthTask_d():
    pass
def fourthTask_e():
    pass
def fourthTask_f():
    pass

if __name__ =='__main__':

    firstTaskLowercaseCount()
    firstTaskUppercaseCount()

    secondTask_a()
    secondTask_b()
    secondTask_c()
    
    thirdTask_a()
    thirdTask_b()
    thirdTask_c()
    thirdTask_d()

    fourthTask_a()
    fourthTask_b()
    fourthTask_c()
    fourthTask_d()
    fourthTask_e()
    fourthTask_f()
