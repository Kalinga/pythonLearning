
class MySimpleClass(object):
    def __init__(self):
        self.__pri = "private: "
        self._pro = "protected: "
        self.pub = "public: "
        self._const = 999

    def sum(self, val):
        return val + self._const

    def __priMethod(self):
        print "This is private method"

if __name__=="__main__":
    obj = MySimpleClass()
    print obj.sum(101)

    # accessing public
    print obj.pub

    # Changing the value of pub attribute
    obj.pub = obj.pub + "we can modify it"

    print obj.pub

    # accessing protected attribute and modifying it

    print obj._pro

    obj._pro = obj._pro + "we can modify it too"

    print obj._pro, "\n 'private' needs a hack to be accessed"

    # trying to access private members

    print obj._MySimpleClass__pri

    #obj.__pri()
    print dir(obj)

    obj._MySimpleClass__priMethod() #name mangling

# Why we need if still we can access private method

# https://mail.python.org/pipermail/tutor/2003-October/025932.html
