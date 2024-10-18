# alps = {chr(i): i for i in range(ord('a'), ord('z') + 1)}

str = '10110111'
val = ''
alps = {}
j = 1
for i in range(ord('A'),ord('Z')+1):
    x = {'1'*j : chr(i)}
    j+=1

    alps.update(x)

print(alps)
count = 0

for i in str:
    if i == 1:
        count+=1
    else:
        zo = '1'*count
        k = alps[zo]
        val += k
        count = 0

val += alps['1'*count]

print(char)
        
