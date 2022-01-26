# 절차지향 
a = [1,2,3]

a = sorted(a)
a= reversed(a)


def append(a, value) :
    return 1 + [value]

a = append(a,4)

person_01 = {
    'name' : '아이유',
    'age' : 20
}
person_02 = {
    'name' : '홍길동',
    'age' : 000
}


def greeting(person) :
    #person : dictionary 
    print('안녕하세요'+person["name"])
greeting(person_01)
print(person_01['name'])