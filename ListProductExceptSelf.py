#238 Medium
def productExceptSelf( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    arr = []
    mul = 1
    for j in nums:
        mul = mul * j
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            multi = 1
            for j in range(0,i):
                multi = multi * nums[j]
            for k in range(i+1,len(nums)):
                multi = multi * nums[k]
            sum = multi
        else:
            sum = mul//nums[i]
        arr.append(sum)

    return arr
        