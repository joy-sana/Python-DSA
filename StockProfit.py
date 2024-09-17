prices = [0, 8, 5, 3,2, 1, 4]

len_arr = len(prices)
min = prices[0]
minIndex = 0
for i in range(0,len_arr):
    if prices[i] < min:
        min = prices[i]
        minIndex = i


print(minIndex)