class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        alps = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        alps2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for i in s:
            if i in alps:
                alps[i] = alps[i] + 1

        for i in t:
            if i in alps2:
                alps2[i] = alps2[i] + 1

        for i in alps:
            if alps[i] < alps2[i]:
                return i


        # Optimized Version
            
        # alps = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
       
        # for i in s:
        #     if i in alps:
        #         alps[i] = alps[i] + 1

        # for i in t:
        #     if i in alps:
        #         alps[i] = alps[i] - 1
        #         if alps[i] < 0:
        #             return i
        