def heading(str):
    print "~" * 80
    offset = (80 - len(str) - 2) / 2
    print "|" + " " * offset + str + " " * offset + "|"
    print "~" * 80