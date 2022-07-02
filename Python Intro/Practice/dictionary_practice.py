lst = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
s = 0
i = 0
while len(lst) !=0:
    a = lst.pop(0) 
    if a >= 80 :
        s += a
print(s)

a  = {'a' : 'ab'}
print(type(a.get('a')))
print(type(a['a']))