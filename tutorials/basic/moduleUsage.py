from sys import exit
from testmodule.exit import *
import os

print "Hey Kalinga: Important modules to re-look are:\n'sys'\n'os'\n'subprocess'\n" * 5

testPath = os.path.join(os.getcwd(), "test.txt")
print "test.txt file path is: ", testPath
print os.path.dirname(testPath)
print os.path.basename(testPath)
print os.path.dirname(os.path.dirname(testPath))
print "Split path: ",  os.path.split(testPath)

print "Demo of using module from my project: \n"
exit()

from sys import exit
print "\nDemo of using module from sys now : \n"
exit()
