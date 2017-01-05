from  project.styleformat import heading

import string

heading("Module 2 Assignments: 1")

total =int(input('\n What is the total amount for your online shopping?'))
country = raw_input('Shipping within the US or Canada?')

if country == "US":
    if total <= 50:
        print "Shipping Costs $6.00"
    elif total <= 100:
        print "Shipping Costs $9.00"
    elif total <= 150:
        print "Shipping Costs $12.00"
    else:
        print "FREE"

if country == "Canada":
    if total <= 50:
        print "Shipping Costs $8.00"
    elif total <= 100:
        print "Shipping Costs $12.00"
    elif total <= 150:
        print "Shipping Costs $15.00"
    else:
        print "FREE"

heading("Module 2 Assignments: 2")
name = raw_input("Enter your name:")
print "Hello " + name

heading("Module 2 Assignments: 3")
f = int(input("Enter the temperature in Fahrenheit:"))
c = 5 * (f - 32)/9
print ("The equivalent celsius is: ") + str(c)

heading("Module 2 Assignments: 4")
h = int(input("Enter Hours: "))
r = float(input("Enter rate: "))
print ("Total Pay: ") + str (h * r)

heading("Module 2 Assignments: 5")
a = [4,7,3,2,5,9]

for index, value in enumerate(a):
    print "index: " + str(index) + str(", ") + "value: " + str(value)

heading("Module 2 Assignments: 6")

upper = list(string.uppercase)
dictUpper = dict(enumerate(upper))
revUpperDect = dict((y,x + 1) for x,y in dictUpper.iteritems())
print revUpperDect

heading("Module 2 Assignments: 7")

dict1 = { 'a': 1, 'b':2 }
dictRev = dict((y,x) for x,y  in dict1.items())
print  dictRev

heading("Module 2 Assignments: 8")
L = ['a', 'b', 'c', 'd']
dictRes = dict((y,x + 1) for x,y in enumerate(L))
print dictRes