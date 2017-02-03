import os

def heading(str):
    print "~" * 80
    offset = (80 - len(str) - 2) / 2
    print "|" + " " * offset + str + " " * offset + "|"
    print "~" * 80

def clear():
    os.system("clear")
    print "|_|_|" * 30

def env():
    os.system("env")

