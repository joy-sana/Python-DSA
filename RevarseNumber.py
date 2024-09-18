# n = 9846512
# rev = 0 
# while n > 0:
#     rev = (rev*10) + (n % 10)
#     n = n//10

# print(rev)


count = 5
if (count ^ 1) == (count + 1):
    index = (count//2) +1
    print("first")
else:
    index = ((count + 1)//2)
    print("second")


print (index)