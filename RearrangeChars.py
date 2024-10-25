
def rearangeChar(str1,t):
    verify = {}

    for i in str1:
        if i not in verify:
            verify[i] = 1
        else:
            verify[i] += 1

    for j in t:
        if j in verify:
            verify[j] -= 1
        else:
            print(2)
            return False 

    for i in verify:
        if verify[i] > 0:
            print(i)
            return False
    return True

def reArangeCharSort(s1,t1):
    s1 = sorted(s1)
    t1 = sorted(t1)
    
    if s1 == t1:
        return True
    else:
        return False
    
s = input().strip()
print(s)
t = 'lislten'
print(rearangeChar(s,t))
print(reArangeCharSort(s,t))