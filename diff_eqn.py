# solution of first order ode y' = x + y
# initial value y(0) = 1


import numpy as np
import matplotlib.pyplot as plt

def dydx(x,y):
    return 10*y*np.sin(x*y**2)

def solution(x0,y0,a,b,n=10000):
    values = [[x0,y0]]
    h = (b-a)/n
    for i in range(n):
        # copy n-th values
        xn, yn = x0, y0
        # n+1 th value
        xn1, yn1 = xn+h, yn+h*dydx(xn,yn)
        # saving data in a list
        values.append([xn1,yn1])
        # redefining previous datas
        x0, y0 = xn1, yn1
    return np.array(values)

x = solution(x0=0,y0=1,a=-2,b=2).T[0]
y = solution(x0=0,y0=1,a=-2,b=2).T[1]

plt.plot(x,y,label=r"$x \:\:vs \:\:f(x)$")
plt.plot(x,dydx(x,y),label=r"$x \:\: vs\:\: \frac{df(x)}{dx}$")
plt.legend()
plt.xlabel(r"$x\longrightarrow$")
plt.ylabel(r"$y\longrightarrow$")
plt.grid()
plt.show()