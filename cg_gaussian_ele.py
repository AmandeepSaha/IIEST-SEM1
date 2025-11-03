# Gauss Elimination Method (General Python Implementation)
# Solves n linear equations with n unknowns: A * x = b

def gauss_elimination():
    # Take number of equations
    n = int(input("Enter number of equations: "))

    # Create augmented matrix
    print("Enter the augmented matrix coefficients (A | b):")
    a = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n + 1:
            raise ValueError("Each row must have n+1 values (coefficients + constant term).")
        a.append(row)

    # Forward elimination
    for i in range(n):
        # Pivot check: if diagonal element is zero, swap with a lower row
        if a[i][i] == 0:
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is singular or has infinite/no solutions.")

        # Normalize pivot row
        pivot = a[i][i]
        for k in range(i, n + 1):
            a[i][k] /= pivot

        # Eliminate below
        for j in range(i + 1, n):
            factor = a[j][i]
            for k in range(i, n + 1):
                a[j][k] -= factor * a[i][k]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]

    # Display solution
    print("\nSolution:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")

# Run the function
if __name__ == "__main__":
    gauss_elimination()
