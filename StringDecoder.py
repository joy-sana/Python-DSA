# alps = {chr(i): i for i in range(ord('a'), ord('z') + 1)}

str = '10110111'
str = '111111110111110111111111111011111111111101111111111111110'
val = ''
alps = {}
j = 1
count = 0


for i in range(ord('A'),ord('Z')+1):
    x = {'1'*j : chr(i)}
    j+=1

    alps.update(x)

for i in str:
    if i == '1':
        count+=1
    else:
        val += alps['1'*count]
        count = 0
if count != 0:
    val += alps['1'*count]  

print(val)
        
