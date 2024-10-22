str = "hello guys it's me joy abdin sana"

charCount = {}

for char in str:
    if char.lower() not in charCount:
        charCount[char] = 1
    else:
        charCount[char.lower()] += 1

# print(charCount)


charCount = dict(sorted(charCount.items(), key = lambda x : x[1], reverse = True))

print(charCount)

j = 0
for i in charCount:
    print(charCount[i])
    j+=1
    if j == 2:
        break