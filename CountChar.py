str = 'HelloWorld'
n = len(str)
find = input('enter the text: ')


count = 0

for i in str:
    if i is find:
        count+=1

print(count)