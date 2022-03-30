def func(combi) :
    if len(combi) == r :
        print(combi)
        return 

    if combi :
        tmp_max = max(combi)
    else :
        tmp_max = 0
    for i in lst :
        if i not in combi  :
            if i<=tmp_max :
                continue
            combi.append(i)
            func(combi)
            combi.pop()


lst = [1,2,3,4,5]
r = 3 

# func([])

def func2(combi,idx) :
    if len(combi) == r :
        print(combi,idx)
        return 

    for i in range(idx+1,len(lst)) :
        combi.append(lst[i])
        func2(combi,i)
        combi.pop() 
func2([],-1)