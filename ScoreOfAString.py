class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # alps = {chr(i): i for i in range(ord('a'), ord('z') + 1)}

        sum = 0
        for j in range(0,len(s)-1):
            val = ord(s[j]) - ord(s[j+1])
            sum  += abs(val)
        
        return sum