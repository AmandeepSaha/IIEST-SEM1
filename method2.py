def f(x):
    return x**3 + 8

def solution(a, b):
    
    for i in range(100000):
        fa, fb = f(a), f(b)
        if fa*fb >= 0:
            raise ValueError("boundary doesn't satisfy")
        else:
            c = b - fb*(b-a)/(fb-fa)
            fc = f(c)

            if fa*fc<0:
                b = c
            else:
                a = c
            if abs(fc)<=0.0000001:
                print("root is ",c, " at iteration ",i)
                break

solution(-100,100)