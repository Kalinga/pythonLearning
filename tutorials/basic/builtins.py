def dirPrint(str=''):
    print "\nprint dir({0}):\n".format(str)
    count = 0
    for item in dir(str):
        count += 1
        print item,
        if count == 5:
            print "\n"
            count = 0

dirPrint()
dirPrint('class')
dirPrint('struct')


def zeroArgs():
    print "This takes no argument\ n"

zeroArgs