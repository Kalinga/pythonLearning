import os

def heading(str):
    print "~" * 80
    offset = (80 - len(str) - 2) / 2
    print "|" + " " * offset + str + " " * offset + "|"
    print "~" * 80

def clear(hint=""):
    os.system("clear")
    print "|"+ "_" * 10 + hint + ("_" * 10) + "|"

def env():
    os.system("env")

