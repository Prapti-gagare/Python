
# creating a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# 1. Append an element
numbers.append(60)
print("After Appending 60:", numbers)

# 2. Insert an element at index 2
numbers.insert(2, 25)
print("After Inserting 25 at index 2:", numbers)

# 3. Remove an element
numbers.remove(40)
print("After Removing 40:", numbers)

# 4. Pop last element
popped = numbers.pop()
print("After Popping Last Element:", numbers)
print("Popped Element:", popped)

# 5. Update an element (change index 1 value)
numbers[1] = 200
print("After Updating index 1 to 200:", numbers)

# 6. Sorting the list
numbers.sort()
print("After Sorting:", numbers)

# 7. Reversing the list
numbers.reverse()
print("After Reversing:", numbers)

# 8. Finding length of the list
print("Length of List:", len(numbers))
