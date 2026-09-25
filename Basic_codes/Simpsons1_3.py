
import numpy as np
import matplotlib.pyplot as plt

# Composite Simpson's 1/3 Rule
def simpsons_rule(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    result = (h / 3) * (
        y[0] + y[-1]
        + 4 * np.sum(y[1:-1:2])
        + 2 * np.sum(y[2:-1:2])
    )

    return result, h


# Function to display graph
def plot_graph(f, a, b, title, filename):

    x = np.linspace(a, b, 400)
    y = f(x)

    plt.figure(figsize=(7, 5))
    plt.plot(x, y, label="Function")
    plt.fill_between(x, y, alpha=0.2)
    plt.axhline(0, linewidth=0.8)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(title)
    plt.grid(True)
    plt.legend()

    plt.savefig(filename, dpi=150)
    plt.show()


# ---------------------------------
# 1. Integral of x^2 from 0 to 2
# ---------------------------------

f1 = lambda x: x**2

I1, h1 = simpsons_rule(f1, 0, 2, 4)
exact1 = 8 / 3
error1 = abs(exact1 - I1)

print("1. Integral of x^2 from 0 to 2")
print("h =", h1)
print("Numerical answer =", I1)
print("Absolute error =", error1)

plot_graph(
    f1, 0, 2,
    "Simpson's Rule: Integral of x^2",
    "graph1.png"
)


# ---------------------------------
# 2. Integral of -x^2 from 0 to 1
# ---------------------------------

f2 = lambda x: -(x**2)

I2, h2 = simpsons_rule(f2, 0, 1, 4)
exact2 = -1 / 3
error2 = abs(exact2 - I2)

print("\n2. Integral of -x^2 from 0 to 1")
print("h =", h2)
print("Numerical answer =", I2)
print("Absolute error =", error2)

plot_graph(
    f2, 0, 1,
    "Simpson's Rule: Integral of -x^2",
    "graph2.png"
)


# ---------------------------------
# 3. Experimental data from 0 to 2
# ---------------------------------

x_data = np.array([0, 0.5, 1.0, 1.5, 2.0])
y_data = np.array([1.00, 1.65, 2.70, 4.48, 7.39])

h3 = 0.5

# Simpson's 1/3 formula for tabulated data
I3 = (h3 / 3) * (
    y_data[0] + y_data[-1]
    + 4 * (y_data[1] + y_data[3])
    + 2 * y_data[2]
)

print("\n3. Experimental data")
print("h =", h3)
print("Numerical answer =", I3)
print("Absolute error = Unknown (exact integral not given)")

# Plot experimental data and interpolated curve
# Piecewise quadratic interpolation for Simpson's rule
x_plot = np.linspace(0, 2, 400)

y_plot = np.interp(x_plot, x_data, y_data)

# Use quadratic interpolation on each pair of intervals
for i, x in enumerate(x_plot):
    if x <= 1:
        xs = x_data[:3]
        ys = y_data[:3]
    else:
        xs = x_data[2:]
        ys = y_data[2:]

    y_plot[i] = (
        ys[0] * (x-xs[1]) * (x-xs[2])
        / ((xs[0]-xs[1]) * (xs[0]-xs[2]))
        + ys[1] * (x-xs[0]) * (x-xs[2])
        / ((xs[1]-xs[0]) * (xs[1]-xs[2]))
        + ys[2] * (x-xs[0]) * (x-xs[1])
        / ((xs[2]-xs[0]) * (xs[2]-xs[1]))
    )

plt.figure(figsize=(7, 5))

plt.plot(
    x_plot, y_plot,
    label="Quadratic approximation"
)

plt.scatter(
    x_data, y_data,
    label="Experimental data"
)

plt.fill_between(x_plot, y_plot, alpha=0.2)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Simpson's Rule: Experimental Data")
plt.grid(True)
plt.legend()

plt.savefig("graph3.png", dpi=150)
plt.show()