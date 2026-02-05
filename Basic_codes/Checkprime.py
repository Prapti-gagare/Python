n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    flag = 1
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break

    if flag == 1:
        print("Prime")
    else:
        print("Not Prime")
