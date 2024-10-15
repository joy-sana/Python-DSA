marks = [50, 60]
# marks = [95] * 50 + [90] * 40 + [85] * 10

n = len(marks)

MarksCollection = {}
studentShifted = 0

for i in marks:
    if i in MarksCollection:
        MarksCollection[i] +=1
    else:
        x = {i : 0}
        MarksCollection.update(x)


top_two_marks = sorted(MarksCollection.keys(),reverse=True)[:2]
print(top_two_marks)

for i in top_two_marks:
    studentShifted+=MarksCollection[i]

print(studentShifted)