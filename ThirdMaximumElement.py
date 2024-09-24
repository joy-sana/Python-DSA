class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 =[]
        nums.sort()

        max = float('-inf')
        for i in nums:
            if i > max:
                max = i
                l1.append(max)
                if len(l1) > 3:
                    l1.pop(0)
      
        if len(l1) != 3:
            return l1[len(l1) - 1]
        return l1[0]


