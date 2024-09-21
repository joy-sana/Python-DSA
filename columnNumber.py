def getColumn(n,chars):
    div = n//26
    rem = n%26
    chars.append(rem)
    if div > 26:
        chars = getColumn(div,chars)
    else:
        chars.append(div)

    return chars

        



num = 28

alphabets = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cols = []
cols = getColumn(num,cols)
print(cols)
column = ''
for i in cols[::-1]:
    column +=alphabets[i]

print(column)

# print(alphabets[div]+alphabets[rem])


# ChatGpt Sollution that works on Leetcode:
# class Solution(object):
#     def convertToTitle(self, columnNumber):
#         """
#         :type columnNumber: int
#         :rtype: str
#         """
#         columnName = ''
        
#         while columnNumber > 0:
#             columnNumber -= 1
#             rem = columnNumber % 26
#             columnName = chr(rem + ord('A')) + columnName
#             columnNumber //= 26

#         return columnName