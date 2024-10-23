str = 'snakewatergunsnakewatergungunwater'
n = len(str)

ch = 0
p1,p2 = 0,0

rounds = []
while ch < n:
    if (str[ch] == 's'):
        ch += 5
        rounds.append('s')
    elif(str[ch] == 'w'):
        ch+=5
        rounds.append('w')
    else:
        ch+=3
        rounds.append('g')


print(rounds)

for i in range(0,len(rounds),2):    # print('round',j,k)
    j = i
    k = i + 1
    if (rounds[j] is 's'):
        if (rounds[k] is 'w'):
            p1 +=1
        else:
            p2+=1

    if (rounds[j] is 'w'):
        if (rounds[k] is 'g'):
            p1 +=1
        else:
            p2+=1

    if (rounds[j] is 'g'):
        if (rounds[k] is 's'):
            p1 +=1
        else:
            p2+=1

    print('points: ',p1,p2)
    


if p1 > p2:
    print('first player win')
else:
    print('second Player win')
