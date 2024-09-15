str = 'joy has   bottle '
strLen = len(str)

res = -1
if strLen == 0:
    res = -2
str2=''


for i in range(0,strLen-1):
    if (str[i].isdigit()):
        str2= str2 + str[i]
        if str[i+1].isalpha():
            str2= str2 + ' '
        if str[i+1].isspace():
            str2= str2 + ' '

list1= str2.split()

for j in range(0,len(list1)):
    list1[j] = int(list1[j])
    
if len(list1) != 0:
    res = max(list1)
    
print(res)
