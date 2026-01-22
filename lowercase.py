word = input("Enter a word: ")
result = ""

for ch in word:
   
    if ch >= 'A' and ch <= 'Z':
        result += chr(ord(ch) + 32)   
    else:
        result += ch                 
print(result)
