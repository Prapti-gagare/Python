n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

sorted_flag = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_flag = False
        break

if sorted_flag:
    print("Array is sorted")
else:
    print("Array is not sorted")
