
def canPlaceFlowers( flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    length = len(flowerbed)

    if length > 1 :
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
            print('first if Executed')
            print(flowerbed)


        for i in range(1,length-1):
            if flowerbed[i] == 0:
                if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    print('2nd if Executed: ',i)

        if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
                    n -= 1
                    flowerbed[length-1] = 1
                    print('3rd if Executed: ',length-1)
    else:
        if  flowerbed[0] == 0:
            n-=1
            
    if n < 1:
        return True
    return False




flowerbed =[0,0]
n = 2

print(canPlaceFlowers(flowerbed,n))