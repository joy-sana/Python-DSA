
import math
n = 6
arr = [64,16, 38, 50,81, 100]

arr2 = []
count =0
for num in arr:
    sqrt_num = int(math.sqrt(num))
    if (sqrt_num ** 2) == num:
        count += 1


print(count)
