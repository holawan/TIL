target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1


#이진탐색기 만들기
def binary_search(target) :
    start = 1 #책의 시작 쪽수
    end = Page #끝 쪽수
    cnt = 1 #반복 횟수
    while start<=end : #찾으려는 부분 처음이 끝보다 작거나 같으면
        middle = (start+end)//2 #middle start+end를 2로 나눈 값의 몫
        if target == middle : #target과 middle이 같으면
            return cnt #반복 횟수 반환
        elif middle > target : #middle이 찾으려는 target보다 크면
            end = middle #마지막 부분을 middle로 갱신
        else : #middle이 찾으려는 target보다 작으면
             start = middle #처음 부분을 middle로 갱신
        cnt +=1
    return False