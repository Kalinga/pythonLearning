from pylab import *
import matplotlib.pyplot as plt
def showscatter():
    x = rand(200)
    y = rand(200)
    size = rand(200) * 100
    color = rand(200)
    scatter(x, y, size, color)
    colorbar()
    show()


x = arange(50) * 2 * pi/50

############################ Line Plots ###########################
def lineplot():
    y = sin(x)
    plot(y)
    xlabel('index')
    ylabel('values')
    show()


############################ Line Formatting ###########################
def line_plot_format():
    plot(x, sin(x), 'y-p')
    plot(x, cos(x), 'y-h')

    xlabel('index')

    show()

############################ Scatter Plots #########################
def scatter_plot():
    y = sin(x)

    scatter(x, y)

    show()

############################ Colored Mapped Scatter Plots ###########
def scatter_plot_colorbar():
    x = rand(200)

    y = rand(200)

    size = rand(200) * 50

    color = rand(200)

    scatter(x, y , size, color)

    colorbar()

    show()

############################ Bar Plots ###########################
def barplot():
    bar(x, sin(x), width = x[1] - x[0])
    show()

############################ Histogram ###########################

def histogram():
    hist(randn(200))
    show()

#showscatter()
#histogram()
#lineplot()
line_plot_format()