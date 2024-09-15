s = "hello"
s = "leetcode"
index=[]
for i in range( 0, len(s)):
    if s[i] in 'aeiouAEIOU' :
        index.append(i)
revIndex = index[::-1]

s = list(s)
for i in range(0, len(index)//2):
    first = int(index[i])
    last = int(revIndex[i])

    char = s[first]
    s[first] = s[last]
    s[last] = char

s = ''.join(s)
print(s)

# x =[1,2,3]
# y = x
# x.append(6)
# print(y)