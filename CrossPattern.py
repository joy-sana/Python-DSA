n = 6
t = n - 2
m = n//2
print("*"+" "*t+"*")

for i in range(1,m):
    t = t -2
    print(" "*i+ "*" + " "*t +"*")

j=0
if n%2 != 0:
    print(" "*m+"*")
    j = 1
 
for i in range(1,m+1):
    print(" "*(m-i) + "*" + " "*j + "*")
    j +=2