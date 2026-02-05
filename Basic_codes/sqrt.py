import math
num = float(input("Enter a number to find its square root: "))
if num < 0:
    print("Square root is not defined for negative numbers in real numbers.")
else:
    sqrt_num = math.sqrt(num)
    print(f"The square root of {num} is {sqrt_num}")
