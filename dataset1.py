# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import numpy as np
import matplotlib.pyplot as plt



def true_fanction(x):
    '''
    >>> true_fanction(0)
    0.0
    '''
    pi = math.pi
    y = math.sin(pi * x * 0.8) * 10

    return y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    xlist = []
    ylist = []
    for num in np.arange(-1,1.1,0.1):
        xlist.append(np.round(num,decimals=1))
        ylist.append(true_fanction(num))
    print(xlist)
    print(ylist)
    figure, plt2= plt.subplots()
    plt2.plot(xlist, ylist, label="sin(pi * x * 0.8) * 10")
    plt2.legend()
    figure.savefig("ex1.1.png")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
