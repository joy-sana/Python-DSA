str = "hello Darjelling naruto hacathalon"
str2 = ''
list = str.split()

for words in list:
    newWords = words[::-1]
    str2 = str2 + newWords + ' '

print(str2)