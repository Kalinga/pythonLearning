#CASE 1
#for..else: else executed
for i in range(12) :
    print "%d * %d : %d" % (i ,i, i ** 2 )
else:
    print("#CASE 1: In else block as the 'for' executed successfully for all candidates \n")

#CASE 2
#for..else..break: else NOT executed
for i in range(12) :
    print "%d * %d : %d" % (i ,i, i ** 2 )
    if (i == 10):
        print("\n")
        print ("calling break..so no else will be called \n")
        break;
else:
    print("else block Not executed as the 'for' did not execute successfully for all candidates\n")

#CASE 3
#for..else..continue: else  executed
for i in range(12) :
    print "%d * %d : %d" % (i ,i, i ** 2 )
    if (i == 10):
        continue;
        print "stmt after continue is skipped" # so this will not be executed
else:
    print("#CASE 3: else  executed because 'for' executed successfully for all candidates \n")

#CASE 4
#while..else: else executed
i  = 0
while i < 12 :
    print "%d * %d * %d: %d" % (i, i ,i, i ** 3 )
    i += 1
else:
    print("#CASE 4: else  executed because 'while' executed successfully for all candidates \n")

#CASE 5
#while..else..continue: else executed
i  = 0
while i < 12 :
    i += 1
    if (i == 10):
        continue;
        print "stmt after continue is skipped" # so this will not be executed
    print "%d * %d * %d: %d" % (i, i, i, i ** 3)
else:
    print("#CASE 5: else  executed because 'while' executed successfully for all candidates \n")

#CASE 6
#while..else: else NOT executed
i  = 0
while i < 12 :
    print "%d * %d * %d: %d" % (i, i ,i, i ** 3 )
    i += 1
    if (i == 10):
        break;
        print "stmt after break is skipped" # so this will not be executed
else:
    print("else not executed because 'while' NOT executed successfully for all candidates")

'''#CASE 7
#while..else: else NOT executed
i  = 0
while i < 12 :
    print "%d * %d * %d: %d" % (i, i ,i, i ** 3 )
    i += 1
    if (i == 10):
        return;
        print "stmt after return is skipped" # so this will not be executed
else:
    print("else not executed because 'while' NOT executed successfully for all candidates")
'''