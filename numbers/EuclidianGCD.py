import math

def gcd(a,b):
    print "a:" + str(a) +", b: "+ str(b)
    if (a == b):
        print "a and b are same!"
        return a;

    if (b == 0):
        return a;

    if (a == 0):
        return b;

    if (a > b):
        return gcd(b, a%b)

    if (b > a):
        return gcd(a, b % a)



def gcd1(a,b):
    print "a:" + str(a) +", b: "+ str(b)
    if (a == b):
        print "a and b are same!"
        return a;

    if (b == 0):
        return a;

    if (a == 0):
        return b;

    if (a > b):

        c = a%b;

        d = ((a/b) + 1) * b - a
        print  "c" + str(c)
        print  "d" + str(d)

        return gcd1(d, b)

    if (b > a):

        c = b%a;

        d = ((b/a) + 1) * a - b
        print  "c" + str(c)
        print  "d" + str(d)

        return gcd1(d, a)

def gcd2(a,b):
    print "a:" + str(a) +", b: "+ str(b)

    if (b == 0):
        return a;

    if (a == 0):
        return b;

    if (a > b):

        c = a%b;

        d = ((a/b) + 1) * b - a
        print  "r: " + str(c)
        print  "s: " + str(d)

        e = d if d<c else c
        print  "min(r,s)" + str(e)

        return gcd2(b, e)

    if (b > a):

        c = b % a;
        if (c == 0):
            return b;
        d = ((b/a) + 1) * a - b
        print  "r: " + str(c)
        print  "s: " + str(d)

        e = d if d < c else c
        print  "min(r,s)" + str(e)

        return gcd2(a, e)

if __name__ == '__main__':
    print '__main__'

    # print gcd(45, 36)
    # print gcd(12345, 67890)
    # print gcd1(12345, 67890)
    #
    # print gcd1(45, 36)
    # print gcd1(3, 13)

    # print gcd(978, 89798763754892653453379597352537489494736)
    # print gcd1(978, 89798763754892653453379597352537489494736)

    #print gcd(1221, 1234567891011121314151617181920212223242526272829)
    #res =  gcd1(1221, 1234567891011121314151617181920212223242526272829)
    res = gcd2(12742, 10534)
    print res