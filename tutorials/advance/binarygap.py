def binaryGap(N):
    binStr = bin(N)
    print binStr
    binRepresentaion = binStr[2:]
    longestCount = 0
    currentCount = 0
    leftBoundary = False
    rightBoundary= False
    for l in binRepresentaion:
        pass
        #print l
        if l == "1":
            if not leftBoundary:
                leftBoundary = True
            else:
                rightBoundary = True

            if rightBoundary:
                if currentCount > longestCount:
                    longestCount = currentCount
                currentCount = 0
        elif leftBoundary:
                currentCount+=1

    return (longestCount)

import math


def solution(A, B):
    # write your code in Python 3.6
    numOfSquare = 0
    for i in range(A, B + 1):
        if isSquare(i):
            numOfSquare += 1

    return numOfSquare


def isSquare(num):
    root = math.sqrt(num)
    if int (root  + 0.5) ** 2 == num:
        return True
    else:
        return False

def duration(t1, t2):
    print t1, t2
    sleepTimeStart = t1[-5:]
    print(sleepTimeStart)

    sleepTimeStartMinute = int(sleepTimeStart[0:2]) * 60 + int(sleepTimeStart[3:])
    print(sleepTimeStartMinute)

    sleepTimeEnd = t2[4:9]
    print(sleepTimeEnd)

    sleepTimeEndMinute = int(sleepTimeEnd[0:2]) * 60 + int(sleepTimeEnd[3:])
    print(sleepTimeEndMinute)
    if t1[0:3] == t2[0:3]:
        print ("same day")
        sleepDuration = sleepTimeEndMinute - sleepTimeStartMinute
    else:
        print ("next day")
        sleepDuration = sleepTimeEndMinute + (24 * 60) - sleepTimeStartMinute

    print sleepDuration
    return sleepDuration

def solution(schedule):
    # write your code in Python 3.6

    print schedule
    print "sorted"
    sch = schedule.splitlines()
    for item  in sch :
        print (item )

    weekday_sort_order= {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    sch.sort(lambda x, y: (weekday_sort_order[x[0:3]] > weekday_sort_order[y[0:3]]) - (weekday_sort_order[x[0:3]] < weekday_sort_order[y[0:3]]) )
    print "sorted with keys"
    for item  in sch :
        print (item )

    for idx, val in enumerate(sch):
        #duration("Mon 05:00-13:00", "Mon 15:00-21:00)")
        #print idx,val
        if (idx + 1 <len(sch)):
            duration(sch[idx], sch[idx +1])

if __name__ == '__main__':
  # print binaryGap(0)
   #print binaryGap(1452)
   #print binaryGap(13242)
   #print binaryGap(34512)
   #print binaryGap(1234562)

  #print solution(2, 17)
  A="""Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00"""
  solution(A)

