import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1, 0, 2, 3, 4, 5, 6])
y = np.array([1, 0, 4, 9, 16, 25, 36])
n = len(x)

xl = np.linspace(0, 20, 1000)

def L_basis(xl, x, i):
    """Compute Lagrange basis polynomial L_i(x) for all xl."""
    l_i = np.ones_like(xl)
    for j in range(len(x)):
        if i != j:
            l_i *= (xl - x[j]) / (x[i] - x[j])
    return l_i

def lagrange_interpolation(x, y, xl):
    """Compute interpolated values at xl."""
    Pn = np.zeros_like(xl)
    for i in range(len(x)):
        Pn += y[i] * L_basis(xl, x, i)
    return Pn

Pn = lagrange_interpolation(x, y, xl)

plt.plot(xl, Pn, label="Lagrange Interpolation")
plt.scatter(x, y, color='red', zorder=5, label="Given Points")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid(True)
plt.show()
