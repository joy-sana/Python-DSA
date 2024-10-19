n = [1,12,1,12,45,45,7,8,7,335,36,36,78,45,9,9,9,9]

alps = {}

for i in n:
    if i in alps:
        alps[i] += 1
    else:
        alps[i] = 1

sorted_dict = dict(sorted(alps.items(), key=lambda item: item[1], reverse=False))


stri = ''
print(sorted_dict.keys())
for i in list(sorted_dict.keys())[-2:]:
    stri += str(i)

print(stri)