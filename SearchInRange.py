# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = -1
        e = -1
        index = 0
        for i in nums:
            if i == target:
                e = index
                if s == -1:
                    s = index
            index+=1
        return [ s,e]
            