n = 5


while(n>9):
    if ((n^1) == (n+1)):
        n = ((n-2)//2)
    else:
        n = n//2

    pass
print(n)