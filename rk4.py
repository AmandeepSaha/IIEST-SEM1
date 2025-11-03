# Damped Harmonic Oscillator using RK4 (no external libraries)

def rk4_damped_oscillator(omega0, b, x0=10.0, v0=0.0, h=0.01, periods=15):
    import math

    # natural period (no damping)
    T0 = 2 * math.pi / omega0
    t_max = periods * T0

    t = 0.0
    x, v = x0, v0

    results = []
    while t <= t_max:
        results.append((t, x, v))

        # define derivatives
        def dxdt(v): return v
        def dvdt(x, v): return -2*b*v - (omega0**2)*x

        # RK4 for x and v
        k1x = h * dxdt(v)
        k1v = h * dvdt(x, v)

        k2x = h * dxdt(v + 0.5*k1v)
        k2v = h * dvdt(x + 0.5*k1x, v + 0.5*k1v)

        k3x = h * dxdt(v + 0.5*k2v)
        k3v = h * dvdt(x + 0.5*k2x, v + 0.5*k2v)

        k4x = h * dxdt(v + k3v)
        k4v = h * dvdt(x + k3x, v + k3v)

        x += (k1x + 2*k2x + 2*k3x + k4x) / 6
        v += (k1v + 2*k2v + 2*k3v + k4v) / 6
        t += h

    return results


# Example: Case (i) ω = 1, b = 1
data = rk4_damped_oscillator(omega0=1, b=1)

# Write results to file
with open("output_case_i.txt", "w") as f:
    f.write("t\t\tx\t\tv\n")
    for t, x, v in data:
        f.write(f"{t:.4f}\t{x:.6f}\t{v:.6f}\n")

print("Results saved to output_case_i.txt")


def estimate_period(data):
    zero_crossings = []
    for i in range(1, len(data)):
        if data[i-1][1] * data[i][1] < 0:  # sign change
            zero_crossings.append(data[i][0])
    if len(zero_crossings) >= 2:
        period = 2 * (zero_crossings[1] - zero_crossings[0])
        freq = 1 / period
        print(f"Estimated Period ≈ {period:.3f}, Frequency ≈ {freq:.3f}")
