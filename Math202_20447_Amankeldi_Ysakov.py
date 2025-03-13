import numpy as np

def f(x):
    return np.sin(x)  # Example function, replace with given function

# Define integration limits
a, b = -np.pi, np.pi
n = 500

# Compute step size
dx = (b - a) / n

# Compute left endpoint approximation
x_left = np.linspace(a, b - dx, n)
integral_left = np.sum(f(x_left) * dx)

# Compute right endpoint approximation
x_right = np.linspace(a + dx, b, n)
integral_right = np.sum(f(x_right) * dx)

print(f"Left Endpoint Approximation: {integral_left}")
print(f"Right Endpoint Approximation: {integral_right}")
