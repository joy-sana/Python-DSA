s = '0P'
str = ''
for i in range(0, len(s)):
    if (s[i].isalpha() or s[i].isdigit()):
        if(s[i].isupper()):
            str += s[i].lower()
        else:
            str += s[i]
print(str)
    
rev = str[::-1]
print(rev == str)