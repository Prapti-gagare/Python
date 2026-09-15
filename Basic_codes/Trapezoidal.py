"""
Trapezoidal Rule for I = ∫[a,b] f(x) dx
Evaluates for n = 1, 2, 4, 8, 16 and builds a comparison table
with step size (h), numerical approximation (I_T), absolute error,
and order of accuracy.
"""

import math

# ---------- User settings ----------
def f(x):
    return x**2          # function to integrate

a, b = 0, 2               # integration limits
n_values = [1, 2, 4, 8, 16]
exact = 8/3                # analytical value of the integral (change if f changes)
# ------------------------------------


def trapezoidal_rule(f, a, b, n):
    """Composite trapezoidal rule with n subintervals (equal step size)."""
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    total = f(x[0]) + f(x[-1])
    total += 2 * sum(f(xi) for xi in x[1:-1])
    I = (h / 2) * total
    return h, I


def build_table(f, a, b, n_values, exact):
    results = []
    for n in n_values:
        h, I_T = trapezoidal_rule(f, a, b, n)
        error = abs(exact - I_T)
        results.append((n, h, I_T, error))
    return results


def order_of_accuracy(results):
    """
    Estimate order p using consecutive errors where h is halved:
        E(h)/E(h/2) = 2^p  =>  p = log2(E(h)/E(h/2))
    """
    orders = [None]  # no ratio for the first row
    for i in range(1, len(results)):
        e_prev = results[i - 1][3]
        e_curr = results[i][3]
        if e_curr == 0:
            orders.append(None)
        else:
            p = math.log2(e_prev / e_curr)
            orders.append(p)
    return orders


def print_table(results, orders):
    print(f"{'n':>4} | {'h':>8} | {'I_T':>12} | {'Error':>12} | {'Order p':>8}")
    print("-" * 55)
    for (n, h, I_T, err), p in zip(results, orders):
        p_str = f"{p:.4f}" if p is not None else "   -"
        print(f"{n:>4} | {h:>8.4f} | {I_T:>12.6f} | {err:>12.6f} | {p_str:>8}")
    print("-" * 55)
    print(f"Exact value of the integral: {exact:.6f}")


if __name__ == "__main__":
    results = build_table(f, a, b, n_values, exact)
    orders = order_of_accuracy(results)
    print_table(results, orders)