n = int(input("Enter the value of n: "))

print("Perfect numbers up to", n, "are:")

for num in range(1, n + 1):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if s == num:
        print(num, end=" ")
