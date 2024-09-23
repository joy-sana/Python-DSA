class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        f = 0
        s = 1
        t = 1
        sum1 = 0
        for i in range(2,n):
            sum1 = f + s + t
            f = s
            s = t
            t = sum1
        return sum1
