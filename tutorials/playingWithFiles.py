import time

with open(r"/var/log/dmesg", 'r') as sudoFile:
    while True:
        contents = sudoFile.read(80)
        if contents:
            print  contents
            # time.sleep(1)
        else:
            break
print "File /var/log/dmesg Close status: " + str(sudoFile.closed)


with open("chinese.txt", 'r') as chinaFile:
    contents = chinaFile.read()
    print "Length of the contents: " + str( len(contents))
    print contents

    print "In Python 2, str is not a string! It's just a sequence of bytes."

    for c in contents:
        print c
    utfStr = contents.decode('utf-8')
    print utfStr
    print "Length of the decode contents: " + str(len(utfStr))

    for c in utfStr:
        print c

    print "The Last character is " + utfStr[2]


with open("chinese.txt", 'rb') as chinaBinary:
    contents = chinaBinary.read()
    print type(contents)
    print contents

