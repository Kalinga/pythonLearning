class Rectangle:
    def __init__(self, color="white", width=10, height=5):
        print "Create a ", color, self, "sized", width, "X", height

class RoundedRectangle(Rectangle):
    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,), kw)


rect = Rectangle(color="green", height=18, width=39)
rect = RoundedRectangle(color="blue", height=18, width=39)
