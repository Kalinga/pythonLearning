#import matplotlib as mpl
from pylab import *

def showplot():
    x = arange(50)* 2 * pi/50
    y = sin(x)
    plot(y)
    xlabel("x-axis")
    ylabel("y-axis")
    show()()

def showscatter():
    x = rand(200)
    y = rand(200)
    size = rand(200) * 100
    color = rand(200)
    scatter(x, y, size, color)
    #colorbar()
    show()

#showplot()
showscatter()