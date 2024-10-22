#failed

s = 'abccdeffghiijjjj'
n = len(s)

alps = []
i = 0
count = 0

while( i < n ) :
    if s[i] not in alps:
        alps.append(s[i])
        i+=1
    else:
        if i > 1:
            count +=1
        i += 1
        
print(count)
        
