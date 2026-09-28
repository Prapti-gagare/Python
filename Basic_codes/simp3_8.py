
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# 1. Experimental data
# ---------------------------------
x = np.array([0, 0.5, 1.0, 1.5, 2.0])
y = np.array([1.00, 1.65, 2.70, 4.48, 7.39])

# Number of subintervals and step size
n = len(x) - 1
h = (x[-1] - x[0]) / n

print("Step size h =", h)

# ---------------------------------
# 2. Simpson's 3/8 Rule
#    First 3 subintervals
# ---------------------------------
I_38 = (3 * h / 8) * (
    y[0] + 3*y[1] + 3*y[2] + y[3]
)

print("Simpson's 3/8 result =", I_38)

# ---------------------------------
# 3. Trapezoidal Rule
#    Remaining 1 subinterval
# ---------------------------------
I_trap = (h / 2) * (y[3] + y[4])

print("Trapezoidal result =", I_trap)

# ---------------------------------
# 4. Total integral
# ---------------------------------
I_total = I_38 + I_trap

print("Final numerical integration =", I_total)

# ---------------------------------
# 5. Plot the graph
# ---------------------------------

# Cubic interpolation for the first 3 subintervals
# using the 4 points from x = 0 to x = 1.5
coeff = np.polyfit(x[:4], y[:4], 3)
cubic = np.poly1d(coeff)

x1 = np.linspace(x[0], x[3], 200)
y1 = cubic(x1)

# Linear interpolation for the last subinterval
x2 = np.linspace(x[3], x[4], 100)
y2 = np.interp(x2, x[3:], y[3:])

# Plot experimental data
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', s=60,
            label='Experimental data', zorder=3)

# Plot cubic curve and trapezoidal straight line
plt.plot(x1, y1, label="Cubic interpolation (3/8 rule)")
plt.plot(x2, y2, label="Linear interpolation (trapezoidal)")

# Shade areas under the curves
plt.fill_between(x1, y1, alpha=0.2,
                 label="Area using Simpson's 3/8")
plt.fill_between(x2, y2, alpha=0.2,
                 label="Area using trapezoidal rule")

# Labels and formatting
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical Integration using Simpson's 3/8 Rule")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Display graph
plt.show()