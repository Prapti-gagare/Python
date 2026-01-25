n = int(input("Enter the value of n: "))

sum_of_cubes = 0
for i in range(1, n + 1):
    sum_of_cubes += i**3

print("Sum of cubes of first", n, "natural numbers =", sum_of_cubes)
