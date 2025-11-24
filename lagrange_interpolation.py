import numpy as np

X, Y = [2,4,5,6,8],[4,16,25,36,64]

def L(x, xi, i):
	l = 1
	for j in range(len(Y)):
		if j != i:
			l*= (x-X[j])/(xi-X[j])
	return  l

def P():
	s = 0
	for i in range(len(Y)):
		s+= Y[i]*L(np.linspace(0,10,100),X[i],i)
	return s
	

print(P())
