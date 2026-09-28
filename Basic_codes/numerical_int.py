
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# 1. LOAD THE IRIS DATASET
# ==========================================================

file_path = "Iris.csv"

df = pd.read_csv(file_path)

print("Original Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Check minimum number of observations
if len(df) < 100:
    raise ValueError("Dataset must contain at least 100 observations.")

# ==========================================================
# 2. DATA CLEANING
# ==========================================================

# Convert petal length to numeric
df["PetalLengthCm"] = pd.to_numeric(
    df["PetalLengthCm"], errors="coerce"
)

# Remove missing values
df = df.dropna(subset=["PetalLengthCm"])
df = df.reset_index(drop=True)

# Check valid observations
if len(df) < 100:
    raise ValueError("Need at least 100 valid observations.")

# ==========================================================
# 3. SELECT 7 SAMPLE POINTS
# ==========================================================

# Select first 7 consecutive observations
sample = df.iloc[:7].copy()

# Independent variable: observation number
x = np.arange(7, dtype=float)

# Dependent variable: petal length
y = sample["PetalLengthCm"].to_numpy(dtype=float)

# Number of intervals
n = len(x) - 1

# Equal spacing
h = 1.0

print("\n========== SELECTED SAMPLE DATA ==========")

print("Point\t x\t Petal Length (cm)")

for i in range(len(x)):
    print(f"{i}\t {x[i]:.0f}\t {y[i]:.2f}")

print("\nNumber of points:", len(x))
print("Number of intervals:", n)
print("Step size h:", h)


# ==========================================================
# 4. TRAPEZOIDAL RULE
# ==========================================================

def trapezoidal_rule(y, h):

    n = len(y) - 1

    result = (h / 2) * (
        y[0]
        + y[n]
        + 2 * np.sum(y[1:n])
    )

    return result


# ==========================================================
# 5. SIMPSON'S 1/3 RULE
# ==========================================================

def simpson_one_third(y, h):

    n = len(y) - 1

    if n % 2 != 0:
        raise ValueError(
            "Simpson's 1/3 requires an even number of intervals."
        )

    odd_sum = np.sum(y[1:n:2])
    even_sum = np.sum(y[2:n:2])

    result = (h / 3) * (
        y[0]
        + y[n]
        + 4 * odd_sum
        + 2 * even_sum
    )

    return result


# ==========================================================
# 6. SIMPSON'S 3/8 RULE
# ==========================================================

def simpson_three_eighth(y, h):

    n = len(y) - 1

    if n % 3 != 0:
        raise ValueError(
            "Simpson's 3/8 requires intervals divisible by 3."
        )

    sum_3 = sum(
        y[i]
        for i in range(1, n)
        if i % 3 != 0
    )

    sum_2 = sum(
        y[i]
        for i in range(3, n, 3)
    )

    result = (3 * h / 8) * (
        y[0]
        + y[n]
        + 3 * sum_3
        + 2 * sum_2
    )

    return result


# ==========================================================
# 7. CALCULATE ALL THREE METHODS
# ==========================================================

trap_result = trapezoidal_rule(y, h)

simpson13_result = simpson_one_third(y, h)

simpson38_result = simpson_three_eighth(y, h)


# ==========================================================
# 8. DISPLAY THEORETICAL CALCULATIONS
# ==========================================================

print("\n========== THEORETICAL CALCULATIONS ==========")

# Trapezoidal
print("\n1. TRAPEZOIDAL RULE")

print("Formula:")
print("I = h/2 * [y0 + yn + 2*sum(interior points)]")

print(
    f"I = {h}/2 * "
    f"[{y[0]:.2f} + {y[-1]:.2f} + "
    f"2*{np.sum(y[1:-1]):.2f}]"
)

print(f"Trapezoidal Integral = {trap_result:.4f}")


# Simpson's 1/3
print("\n2. SIMPSON'S 1/3 RULE")

odd_sum = np.sum(y[1:n:2])
even_sum = np.sum(y[2:n:2])

print("Formula:")
print("I = h/3 * [y0 + yn + 4*odd_sum + 2*even_sum]")

print(
    f"I = {h}/3 * "
    f"[{y[0]:.2f} + {y[-1]:.2f} + "
    f"4*{odd_sum:.2f} + 2*{even_sum:.2f}]"
)

print(f"Simpson's 1/3 Integral = {simpson13_result:.4f}")


# Simpson's 3/8
print("\n3. SIMPSON'S 3/8 RULE")

sum_3 = sum(
    y[i] for i in range(1, n)
    if i % 3 != 0
)

sum_2 = sum(
    y[i] for i in range(3, n, 3)
)

print("Formula:")
print("I = 3h/8 * [y0 + yn + 3*sum3 + 2*sum2]")

print(
    f"I = 3*{h}/8 * "
    f"[{y[0]:.2f} + {y[-1]:.2f} + "
    f"3*{sum_3:.2f} + 2*{sum_2:.2f}]"
)

print(f"Simpson's 3/8 Integral = {simpson38_result:.4f}")


# ==========================================================
# 9. COMPARISON TABLE
# ==========================================================

results = pd.DataFrame({
    "Method": [
        "Trapezoidal Rule",
        "Simpson's 1/3 Rule",
        "Simpson's 3/8 Rule"
    ],
    "Integral": [
        trap_result,
        simpson13_result,
        simpson38_result
    ]
})

print("\n========== COMPARISON TABLE ==========")

print(results.to_string(index=False))


# ==========================================================
# 10. GRAPH 1: ORIGINAL DATA POINTS
# ==========================================================

plt.figure(figsize=(10, 5))

plt.plot(
    x, y,
    marker="o",
    linestyle="-",
    label="Observed petal length"
)

plt.xlabel("Observation Number")
plt.ylabel("Petal Length (cm)")
plt.title("Iris Dataset: Selected 7 Observations")

plt.xticks(x)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# ==========================================================
# 11. GRAPH 2: TRAPEZOIDAL RULE
# ==========================================================

plt.figure(figsize=(10, 5))

plt.plot(
    x, y,
    "o-",
    label="Observed data"
)

# Draw and shade individual trapezoids
for i in range(n):

    x_trap = [x[i], x[i], x[i+1], x[i+1]]
    y_trap = [0, y[i], y[i+1], 0]

    plt.fill(
        x_trap,
        y_trap,
        alpha=0.25
    )

plt.xlabel("Observation Number")
plt.ylabel("Petal Length (cm)")

plt.title(
    f"Trapezoidal Rule\nIntegral = {trap_result:.4f}"
)

plt.xticks(x)
plt.grid(True)
plt.legend(["Observed data"])
plt.tight_layout()
plt.show()


# ==========================================================
# 12. GRAPH 3: SIMPSON'S 1/3 RULE
# ==========================================================

plt.figure(figsize=(10, 5))

plt.plot(
    x, y,
    "o",
    label="Observed data"
)

# Fit a quadratic through every 3 points
for i in range(0, n, 2):

    x_group = x[i:i+3]
    y_group = y[i:i+3]

    coefficients = np.polyfit(
        x_group,
        y_group,
        2
    )

    polynomial = np.poly1d(coefficients)

    x_fine = np.linspace(
        x_group[0],
        x_group[-1],
        100
    )

    y_fine = polynomial(x_fine)

    plt.plot(
        x_fine,
        y_fine,
        label="Quadratic approximation"
        if i == 0 else None
    )

    plt.fill_between(
        x_fine,
        y_fine,
        0,
        alpha=0.15
    )

plt.xlabel("Observation Number")
plt.ylabel("Petal Length (cm)")

plt.title(
    f"Simpson's 1/3 Rule\nIntegral = {simpson13_result:.4f}"
)

plt.xticks(x)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# ==========================================================
# 13. GRAPH 4: SIMPSON'S 3/8 RULE
# ==========================================================

plt.figure(figsize=(10, 5))

plt.plot(
    x, y,
    "o",
    label="Observed data"
)

# Fit a cubic through every 4 points
for i in range(0, n, 3):

    x_group = x[i:i+4]
    y_group = y[i:i+4]

    coefficients = np.polyfit(
        x_group,
        y_group,
        3
    )

    polynomial = np.poly1d(coefficients)

    x_fine = np.linspace(
        x_group[0],
        x_group[-1],
        100
    )

    y_fine = polynomial(x_fine)

    plt.plot(
        x_fine,
        y_fine,
        label="Cubic approximation"
        if i == 0 else None
    )

    plt.fill_between(
        x_fine,
        y_fine,
        0,
        alpha=0.15
    )

plt.xlabel("Observation Number")
plt.ylabel("Petal Length (cm)")

plt.title(
    f"Simpson's 3/8 Rule\nIntegral = {simpson38_result:.4f}"
)

plt.xticks(x)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# ==========================================================
# 14. GRAPH 5: COMPARISON OF THREE METHODS
# ==========================================================

plt.figure(figsize=(9, 5))

plt.bar(
    results["Method"],
    results["Integral"]
)

plt.xlabel("Numerical Integration Method")
plt.ylabel("Approximate Integral")

plt.title("Comparison of Numerical Integration Methods")

plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()


# ==========================================================
# 15. SAVE RESULTS TO CSV
# ==========================================================

results.to_csv(
    "iris_integration_results.csv",
    index=False
)

print("\nResults saved to iris_integration_results.csv")
print("\nProgram completed successfully.")