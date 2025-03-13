import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)  # Example function

# Integration limits
a, b = -2, 2
n = 10000  # Number of samples

# Monte Carlo Integration
x_samples = np.random.uniform(a, b, n)
y_samples = np.random.uniform(0, 1, n)
under_curve = y_samples < f(x_samples)

monte_carlo_result = (b - a) * np.mean(under_curve)

# Plot the function and samples
x_plot = np.linspace(a, b, 1000)
y_plot = f(x_plot)

plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label='f(x) = exp(-x^2)', color='blue')
plt.scatter(x_samples, y_samples, c=under_curve, cmap='coolwarm', alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Monte Carlo Integration')
plt.show()

print(f"Monte Carlo Approximation: {monte_carlo_result}")
