data = input().split('-')
s= 0
print(data)
for i in data[0].split('+'):
     s += int(i)
print(s)
for i in data[1:]:
     for j in i.split('+'):
          s -= int(j)

print(s)
