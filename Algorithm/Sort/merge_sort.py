def merge_sort(lst) :
    #길이가 1이면 리턴 
    if len(lst) == 1 :
        return lst 

    #길이가 1보다 크면 중앙을 잡고 
    middle = len(lst)//2 

    #왼쪽과 오른쪽으로 나눔 
    left = lst[:middle] 
    right = lst[middle:]

    #아직 정렬하지 않았지만 코드가 끝나면 정렬 되어 있을 것이다?
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right) :
    result = []

    #모든 아이들을 res에 담을 때 까지 
    while left or right :
        if left and right :
            if left[0] <=right[0] :
                result.append(left.pop(0))
            else :
                result.append(right.pop(0))
        elif left :
            result.extend(left)
            break
        elif right :
            result.extend(right)
            break 
    return result


data = [7,5,3,1,4,2,6,8]
x  = merge_sort(data)
print(x)
print(data)