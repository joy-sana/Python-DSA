# d = {'joy' : 18, 'sourya' :40, 'ashik' : 100}
# d2 = {'deep' : 38}
# n = input('enter a key: ')

# d.update(d2)

# if n in d.keys():
#     print("present", d[n])
#     d[n] += 1
# else:
#     print("not present")
# print(d)

# sum1 = 0  
# for i in d:
#     sum1 += d[i]

# print(sum1)

# l1 = [1,2,3,4,5, 6]
# l2 = ['a', 'b', 'c', 'd', 'e', ' ']

# m = {}
# for i in range(0,len(l1)):
#     x = {l1[i] : l2[i]}
#     m.update(x)

# print(m)

# nums = [2,2,1,1,1,2,2]
# d = {}
# for i in nums:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         x = {i : 1}
#         d.update(x)
# print(d)


# max = float('-inf')
# max_key = float('-inf')
# for i in d:
#     if d[i] > max:
#         max = d[i]
#         max_key = i
#         print('val: ',max)
# print(max_key)


# for key, value in d.items():
#     if value > max:
#         max = value
#         max_key = key
#         # print('val: ',max)
# print(max_key)
    

nums = [1,2]
# l1.pop(0)
# print(l1)

l1 =[]
nums.sort()
print(nums)
max = float('-inf')
for i in nums:
    if i > max:
        max = i
        l1.append(max)
        print('val: ', max)
        if len(l1) > 3:
            l1.pop(0)
print(l1[0])


