n = 5
votes = [1,1,2,2,3]
ages = [13,14,15,16,17]
# votes = [1,1,2,3,4,1,2,2,3,1]
# ages = [24,13,35,15,50,16,20,18,25,64]

Eligible = []
frequncy = {}
i = 0
for age in ages:
    if age >= 18:
        Eligible.append(votes[i])
    i+=1

# print(Eligible)
temp = {}
for candidate in Eligible:
    if candidate not in frequncy:
        temp = {candidate : 1}
        frequncy.update(temp)
    else:
        frequncy[candidate] += 1


print(frequncy)

if not frequncy:
    print(-1)
else:
    max = float('-inf')
    for k,j in frequncy.items():
        if j > max:
            max = j
            winner = k
        
    check = 0
    for k,j in frequncy.items():
        if j == max:
            winner = k
            check += 1
    if check < 2:
        print(winner)
    else:
        print(-1)

