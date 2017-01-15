import math

'''my docs'''
class MyClass(object):
    a = 100
    def exp(self):
        return 100

#instatiating MyClass
obj = MyClass()
print obj
print type(obj)

print obj.exp()
print math.exp(1)

for key in MyClass.__dict__:
    print key, MyClass.__dict__[key]

for key,value in MyClass.__dict__.items():
    print key, value


print MyClass.__dict__
print MyClass.__module__
print MyClass.__base__


class MyClass1(object):
    pass

class OtherClass ( MyClass1, MyClass):
    pass

print OtherClass.__base__
print OtherClass.__bases__

class Student(object):
    def __init__(self, name, age):
        print self
        print "~" * 30

        self.age = name
        self.name = age
        self.python = "Kalinga"

        print "+" * 80 , "\n", self.__class__

    @staticmethod
    def printLine():
        print "\n", "*" * 80

obj = Student(32, "Kalinga")
print obj
obj.printLine()
obj.python
print obj.name