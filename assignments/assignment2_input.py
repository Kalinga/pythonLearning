from  project.styleformat import heading

import string

heading("Module 2 Assignments: 1")
total = int(input('\n What is the total amount for your online shopping?'))
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
print "Hello " + str(name)

heading("Module 2 Assignments: 3")
f = float(input("Enter the temperature in Fahrenheit:"))
c = 5 * (f - 32.0)/9
print ("The equivalent celsius is: ") + str(c)

heading("Module 2 Assignments: 4")
h = float(input("Enter Hours: "))
r = float(input("Enter rate: "))
print ("Total Pay: ") + str (h * r)
