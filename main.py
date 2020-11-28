import math
import libf
def f(y,x):
    z=y*2/x
    return z


def eulerm(x0,y0):
    h=0.01
    x,y=[],[]
    y.append(y0)
    x.append(x0)
    for i in range(1,1000000):
        z=y[i-1]+(h*f(y[i-1],x[i-1]))
        y.append(z)
        x.append(x0+(i*h))
    libf.write_csv("data.csv", y, x)

eulerm(3,1)

