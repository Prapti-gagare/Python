s = input("Enter a string: ")
flag = True
n = len(s)

for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        flag = False
        break

if flag:
    print("Palindrome")
else:
    print("Not a palindrome")
