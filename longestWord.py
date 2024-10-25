str1 = "power respect banana"
words = str1.split()

max = float("-inf")
for i in words:
    if len(i) > max:
        max = len(i)
        word = i

print(word)

