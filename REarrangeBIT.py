# Output Specification:

# Return an integer value representing the minimum possible number that can be 
# formed after re-arranging the bits of the number N.

# Example 1:

# input1: 10
# Output: 3

n = 0
temp = n
count = 0
sum = 0
while(temp > 1):
    digit = temp%2
    rev = temp//2
    temp = rev
    if digit == 1:
        count+=1
if temp == 1:
    count+=1


for i in range(count):
    sum = sum + 2**i

print(sum)