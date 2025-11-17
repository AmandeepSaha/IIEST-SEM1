import numpy as np

def solution(a, b, c):
    D = np.lib.scimath.sqrt(b**2 - 4*a*c)  # handles negative discriminant
    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)
    return [x1, x2]

print(solution(float(input("a= ")), float(input("b= ")), float(input("c= "))))
