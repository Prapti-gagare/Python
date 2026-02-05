n = int(input("Enter a natural number: "))

sum_sq = 0
for i in range(1, n + 1):
    sum_sq += i * i

print("Sum of squares of first", n, "natural numbers =", sum_sq)
