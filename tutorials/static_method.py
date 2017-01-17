
class TeachMe(object):
    def __init__(self, param):
        #print "__init__:",param,"->", self
        self.param = param

    def instance_method(self, param):
        self.name = param
        print TeachMe.static_method(param)

    @staticmethod
    def static_method(param):
        return param*2

    @classmethod
    def class_method(cls, param):
        return param*3

#calling static method using class name
print TeachMe.static_method("Static method ")
#calling class method using class name
print TeachMe.class_method("Class method ")

obj1 = TeachMe(10)
obj2 = TeachMe(10)
print (obj1 == obj2)

print "static " * 10
print TeachMe(100).static_method
print TeachMe(200).static_method
print (TeachMe(100).static_method is TeachMe(200).static_method)
print (TeachMe(100).static_method is TeachMe.static_method)
print (TeachMe(100).static_method == TeachMe(200).static_method)
s1 = TeachMe(100).static_method
s2 = TeachMe(200).static_method
print id(s1)
print id(s2)


print "instance " * 10

print TeachMe(300).instance_method
print TeachMe(400).instance_method

print (TeachMe(400).instance_method is TeachMe(500).instance_method)
print (TeachMe(400).instance_method is TeachMe.instance_method)
print (TeachMe(400).instance_method == TeachMe(500).instance_method)
i1 = TeachMe(100).instance_method
i2 = TeachMe(200).instance_method
print id(i1)
print id(i2)

print "class " * 10

print TeachMe(300).class_method
print TeachMe(400).class_method

print (TeachMe(400).class_method is TeachMe(500).class_method)
print (TeachMe(400).class_method is TeachMe.class_method)
print (TeachMe(400).class_method == TeachMe(500).class_method)
c1 = TeachMe(100).class_method
c2 = TeachMe(200).class_method
c3 = TeachMe.class_method
print id(c1)
print id(c2)
print id(c3)