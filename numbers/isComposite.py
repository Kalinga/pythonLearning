import math
import sympy

def isComposite(input):
    return not sympy.isprime(input)

def countSequence(start, end):

    prevCount = 0
    count = 0
    seq = []
    prevseq = []
    for i in range(start, end):
        if (isComposite(i)):
            count = count +1
            seq.append(i)
        else:
            if prevCount < count:
                prevCount = count
                prevseq = seq

            count = 0
            seq = []
    if len(prevseq)> len(seq):
        seq = prevseq
    for i in range(0, len(seq)):
        print seq[i],

    return count if count > prevCount else prevCount

def countIn_n_bitRange(n):
    print "For ", n, " bit number"
    start = int(math.pow(2, n))
    end = int(math.pow(2, n+1))
    print "start,end", start, end

    count_n = countSequence(start, end)
    print "\n","sequence count is: ", count_n,"\n"


if __name__ == '__main__':
    if __name__ == '__main__':
        print isComposite(221)

        # countIn_n_bitRange(2) #1
        # countIn_n_bitRange(3) #3 #K3 = 3
        # countIn_n_bitRange(4) #5 #K4 = 5
        # countIn_n_bitRange(5) #5 #K5 = 5
        #
        # countIn_n_bitRange(6) #13 #K6 = 13
        # countIn_n_bitRange(7) #11 #K7 = 11
        # countIn_n_bitRange(8) #13 #K8 = 13
        # countIn_n_bitRange(9) #19 #K9 = 19

        # countIn_n_bitRange(10) #33  #!
        # countIn_n_bitRange(11) #27  #!
        # countIn_n_bitRange(12) #31 #K10 = 31
        # countIn_n_bitRange(13) #43 #K11 = 43

        #countIn_n_bitRange(14) # 71 #K112 = 71
        #countIn_n_bitRange(15) # 61 #K13 = 61
        #countIn_n_bitRange(16) # 63  #!
        #countIn_n_bitRange(17) # 85  #!

        # countIn_n_bitRange(18) # 113 #K14 = 113
        # countIn_n_bitRange(19) # 99   #!
        # countIn_n_bitRange(20) # 147  #!
        # countIn_n_bitRange(21) # 137 #K15 = 137

        # countIn_n_bitRange(22)  # 153 #!
        # countIn_n_bitRange(23)  # 153 #!
        # countIn_n_bitRange(24)  # 209 #!
        # countIn_n_bitRange(25)  # 219 #!
        # countIn_n_bitRange(26)  # 221 #!

        #Finding K16 is much more difficult due to the knownn fact that density of a prime number decreseas as n grows
