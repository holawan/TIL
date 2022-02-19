def bubble_sort(num):
    #원소의 마지막 -1부터
    #why? 최대값부터 마지막에 박고 오름차순으로 정렬할 것이기 때문
    for i in range(len(num)-1,0,-1) :
        #0번 index부터 i번째 index까지
        for j in range(0,i) :
            #num[j]가 num[j+1]보다 크면
            if num[j] > num[j+1] :
                #위치 변경
                num[j],num[j+1] = num[j+1],num[j]
    return num
num = [54,26,93,17,77,31,44,55,20]

print(bubble_sort(num))