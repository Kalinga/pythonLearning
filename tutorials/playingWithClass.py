import math

from project import styleformat


class MyClass(object):
    '''my docs'''
    a = 100
    def exp(self):
        return 100

#instatiating MyClass
student = MyClass()
print student
print type(student)

print student.exp()
print math.exp(1)

styleformat.heading("__dict__: Output")
for key in MyClass.__dict__:
    print key, MyClass.__dict__[key]

for key,value in MyClass.__dict__.items():
    print key, value

print MyClass.__dict__

styleformat.heading("__module__, __base__, __doc__: Output")
print MyClass.__module__
print MyClass.__base__
print MyClass.__doc__


class MyClass1(object):
    pass

class OtherClass ( MyClass1, MyClass):
    pass

styleformat.heading("OtherClass __base__, __bases__: Output")
print OtherClass.__base__
print OtherClass.__bases__

class Student(object):
    #. Class Variables
    #. Static Methods
    #. Class Methods
    #. Ctor
    #. Dtor
    #. Instance Methods

    @staticmethod
    def print__init__OverloadingSignature():
        styleformat.heading("Overloading signature of __init__(self, *args, **kwargs[])")

    @classmethod
    def classMethod(cls):
        print "\n", "This is a class method"
        print "cls: ", cls

    def __init__(self, name, age):
        styleformat.heading("class Student.__init__")
        print self

        self.age = name
        self.name = age

        print "self.__class__:", self.__class__

    def instanceFunction(self):
        print "instanceFunction"

student = Student(32, "Kalinga")
print student
Student.print__init__OverloadingSignature()
Student.classMethod()

print "Student name: ", student.name
student.userDefinedAttrib = "'This is a user defined attribute'"
print  student.userDefinedAttrib

styleformat.heading("__init__ can also be called explicitly !!DON'T DO THAT!!!")
student.__init__("Bhusan", 33)
print "Student name: ", student.name

print dir (student)
print dir(Student)



