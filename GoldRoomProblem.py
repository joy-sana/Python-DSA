n = 10
k = 15
coins = [5,3,7,14,18,1,18,4,8,3]

i = 0
j = 0
sum = 0
while(j<n):
   
# coins = [0,1,2, 3, 4,5, 6,7,8,9]
# coins = [5,3,7,14,18,1,18,4,8,3]
    if sum > k:
        i+=1
        sum -= coins[i]
        print("sum greter than k",i,j,sum)
    if sum < k:
        sum += coins[j] 
        j+=1
        print("sum less than k",i,j,sum)

    if sum == k:

        print("index found",i+1 ," ,",j)
        sum -= coins[i]
        i+=1