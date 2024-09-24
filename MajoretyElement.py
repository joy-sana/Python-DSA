nums =[6,5,5]
d = {}
for i in nums:
    if i in d.keys():
        d[i] += 1
        # if d[i] > (len(nums)//2):
        #     return i
    else:
        x = {i : 1}
        d.update(x)
    
max = float('-inf')
max_key = float('-inf')
for i in d:
    if d[i] > max:
        max = d[i]
        max_key = i
        # print('val: ',max)
print(max_key)