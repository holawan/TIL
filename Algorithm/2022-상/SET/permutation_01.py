lst = [1,0,0,1,1]

r = 5

#내부 반복이 없는 경우 
def func(perm) :
    if len(perm) == r :
        print(perm)
        return
    for i in lst :
        if i not  in perm :
            perm.append(i) 
            func(perm)
            perm.pop()

# func([])

#중복조합
def func2(perm) :
    if len(perm) == r :
        print(perm)
        return
    for i in lst :
        perm.append(i) 
        func2(perm)
        perm.pop()

func2([])
