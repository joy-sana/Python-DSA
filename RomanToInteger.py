# https://leetcode.com/problems/roman-to-integer/description/
s = "MCMXCIV"

symbols = {
    'I' :  1,
    'V' :  5,
    'X' :  10,
    'L' :  50,
    'C' :  100,
    'D' :  500,
    'M' :  1000
}
# s = "0123456"
# s = "MCMXCIV"
# s = "LVIII"
final_sum = symbols[s[0]]
for i in range(1,len(s)):
    final_sum += symbols[s[i]]
    if symbols[s[i]] > symbols[s[i-1]]:
        final_sum -= (2 * symbols[s[i-1]])
print( final_sum)