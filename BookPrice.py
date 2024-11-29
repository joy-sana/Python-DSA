prices = [15, 5, 10, 25, 20, 30] #(15,10),(15,20), (5,10), (25,20), (25,30)
k = 5

fd = {} #frequecny dict
count = 0

for price in prices:
    if price in fd:
        fd[price] += 1
    else:
        fd[price] = 1


for price in prices:
    if (price + k) in fd:
        count += fd[price + k]

print(count)