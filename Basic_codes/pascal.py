n = int(input("Enter number of rows: "))

pascal = []

for i in range(n):
    row = [1] * (i + 1)  
    for j in range(1, i):
        row[j] = pascal[i-1][j-1] + pascal[i-1][j]
    pascal.append(row)

print("\nPascal Triangle:")
for i in range(n):
    print(" " * (n - i - 1), end="")
    for num in pascal[i]:
        print(num, end=" ")
    print()
