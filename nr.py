def f(x):
    return x**2-9

def df(x):
    return 2*x

def solution_nr(n=1000, x0=1):
    xn = x0
    for i in range(n):
        xn1 = xn - f(xn)/df(xn)
        
        if abs(xn1-xn) < 0.00000001:
            print(xn1," at iteration ",i+1)
            break
        
        xn = xn1
    return xn

solution_nr()