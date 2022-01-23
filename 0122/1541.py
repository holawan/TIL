data = input().split('-')

s1 = []

for i in data :
    data2 = i.split('+')
    s = 0
    for j in data2 :
        s += int(j)
    s1.append(s)
result = s1[0]
for i in s1[1:] :
    result -= i
print(result)