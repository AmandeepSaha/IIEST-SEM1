# eqn: d2x/dt2 + 2b dx/dt + x = 0


import numpy as np
import matplotlib.pyplot as plt


# state vector
def S(t, x, v, b):
	return [
		v,
		-2*b*v - x
	]

# solution using kr4 method
def rk_four(t0, v0, x0, tn, b, h= 10e-4):
	
	t, v, x = t0, v0, x0			# initial conditions
	n = int(np.abs(t0-tn)/h)		# number of iterations
	values = [[t, x, v]]			# to store time, position, velocity
	
	for _ in range(n):
		
		k1x, k1v = S(t, x, v, b)
		
		k2x, k2v = S(t, x+0.5*k1x*h, v+0.5*k1v*h, b)
		
		k3x, k3v = S(t, x+0.5*k2x*h, v+0.5*k2v*h, b)
		
		k4x, k4v = S(t, x+h*k3x, v+h*k3v, b)
		
		kx = h*(k1x + 2*k2x + 2*k3x + k4x)/6
		kv = h*(k1v + 2*k2v + 2*k3v + k4v)/6
		
		t += h
		x += kx
		v += kv
		
		values.append([t, x, v])
		
	return {
			"time": np.array(values).T[0], 
			"position":np.array(values).T[1], 
			"velocity":np.array(values).T[2]
			}


# your rk_four and S must be defined above this

if __name__ == "__main__":
    b_values = [1, 4, 0.1, 20]

    fig, ax = plt.subplots(2, 2, figsize=(10, 8))

    # IMPORTANT — flatten the 2×2 array into 1D array of axes
    ax = ax.flatten()

    for index, b in enumerate(b_values):
        sol = rk_four(0, 0, 10, 30, b)   # (t0, v0, x0, tn, b)

        t = sol["time"]
        x = sol["position"]
        v = sol["velocity"]

        ax[index].plot(t, x, label="x(t)")
        ax[index].plot(t, v, label="v(t)")
        ax[index].set_title(f"Damping b = {b}")
        ax[index].set_xlabel("t")
        ax[index].legend()
        ax[index].grid(True)

    plt.tight_layout()
    plt.show()
