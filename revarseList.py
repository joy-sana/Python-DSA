s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
l = len(s)-1
for i in range (0, len(s)//2):
    char = s[i]
    s[i] = s[l-i]
    s[l-i] = char

print(s)