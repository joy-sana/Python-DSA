# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
def isAnagram(s, t):
    newS = list(s)
    newT = list(t)
    countT = 0
    countS = 0
    newS.sort()
    newT.sort()
    if len(newS) == len(newT):
        for i in range(0,len(newT)):
            if newS[i] != newT[i]:
                return False
        return True
    return False


s = 'aaca'
t = 'ccaa'
# newS = list(s)
# newS.sort()
print(isAnagram(s,t))
