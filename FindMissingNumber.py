nums = [0,1,2,4,5,6,7]
length = len(nums)
sum1 = 0
actual = (length * (length+1)) // 2

for i in range(0,length):
    sum1+=nums[i]

print(sum(nums))
print(sum1)
print(actual)

print('Missing number: ', actual - sum1)