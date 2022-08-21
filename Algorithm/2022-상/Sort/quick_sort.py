def quick_sort(lst,l,r) :
    if l<r: 
        pivot = hoare_partition(lst,l,r)
        quick_sort(lst,l,pivot-1)
        quick_sort(lst,pivot+1,r)

def hoare_partition(lst,l,r) :
    pivot = lst[l]
    i = l 
    j = r 

    while i<=j :
        #i랑 j가 만나거나 pivot이 lst[i]보다 크면 반복 
        while i<=j and lst[i] <= pivot :
            i += 1 
        while i<=j and lst[j] >pivot :
            j -= 1 
        if i < j :
            lst[i],lst[j] = lst[j],lst[i]
        lst[l],lst[j] = lst[j],lst[l]

    return j 


def lomuto_partition(lst,l,r) :
    pivot = lst[r]
    i = l-1 

    for j in range(l,r) :
        if lst[j] <=pivot :
            i += 1 
            lst[j], lst[i] = lst[i], lst[j]

    lst[r] , lst[i+1] = lst[i+1], lst[r]

    return i +1 

data = [7,5,3,1,4,2,10,3,6,9,8]
quick_sort(data, 0, len(data)-1)
print(data)