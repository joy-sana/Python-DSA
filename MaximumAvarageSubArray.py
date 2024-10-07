#643
def findMaxAverage( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    i,j,sum = 0,0,0
    n = k
    
    while n > 0:
        sum += nums[j]
        j+=1
        n-=1
        MaxE = sum

    while(j < len(nums)):
        sum = sum - nums[i] 
        sum = sum + nums[j] 

        if( MaxE < sum):
            MaxE=sum
        i += 1
        j += 1    
        
    final = float(MaxE)/float(k)
    return final


n = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(n,k))
