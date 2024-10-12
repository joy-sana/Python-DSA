
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","c"]
# chars = ["a","a","b","b","c","c","c"]
alps = {}
for i in chars:
    if i in alps:
        alps[i] += 1
    else:
        alps[i] = 1
print(alps)
pos = 0
index = 0
i = 0
tempCount = 1
j = 1

while(j < len(chars)):
    if chars[i] is chars[j]:
        tempCount += 1
        print('counting',tempCount)
    
    elif (chars[i] != chars[j]) or j == len(chars):
        chars[index] = chars[i]
        index += 1
        if tempCount == 1:
            pos += 1
            print('one')

        if tempCount < 10:
            print('Index : ',index,tempCount)
            chars[index] = str(tempCount)
            index += 1
            pos += 2
            tempCount = 1
        else:
            tempStr = str(tempCount)
            pos += 1
            for i in tempStr:
                chars[index] = i
                index += 1
                pos += 1
            tempCount = 1
        
    i += 1
    j += 1
   

# print(pos)
print(chars[:pos])
    
