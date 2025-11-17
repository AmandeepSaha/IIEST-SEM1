def f(x):
    return 2*x + 4

def solution(a,b):
    
    for i in range(1000):
        fa, fb = f(a), f(b)
        if fa*fb>0:
            raise ValueError("boundary is not satisfying condition")
        else:
            
            c = (b+a)/2
            fc = f(c)
            
            if fc*fa<0:
                b = c
            else:
                a = c
            if abs(fc)<=0.0001:
                print("root is ", round(c,3), " at iteration ", i)
                break

solution(-100,100)