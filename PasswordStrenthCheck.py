str = "s@#4f"
specialChar = ['@', '!','#','%','^', '&', '*']

n = len(str)
specialCharCount = 2
size = 1
low = 1
capital = 1
numeric = 1
repeat = 0

dict = {}


if (n < 23) and (n > 5):
    size = 0


i = 0
while(i < n):
    if(i < n):
        if (str[i].islower()):
            low = 0
            i+=1

    if(i < n):
        if str[i].isupper():
            capital = 0
            i+=1

    if(i < n):
        if str[i].isnumeric():
            numeric = 0
            i+=1
            
    if(i < n):
        if str[i] in specialChar:
            specialCharCount -= 1
            i+=1

for char in str:
    if char not in dict:
        x = {char : 1}
        dict.update(x)
    else:
        dict[char] += 1

for i in dict:
    if dict[i] > 1:
        repeat = 1
        break


if specialCharCount > 0:
    final = 1 + numeric + capital + low + repeat + size
else:
    final = 0 + numeric + capital + low + repeat + size

print(final)