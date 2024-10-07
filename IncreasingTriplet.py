def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    j = 1
    k = 2
    for i in range(0,len(nums)-2):
        print(i,j,k,"__",nums[i],nums[j],nums[k])
        if nums[i] < nums[j] < nums[k]:
            return True
        j+=1
        k+=1
    return False

n = [20,100,10,12,5,13]

print(increasingTriplet(n))