def counting_sort(input_arr,k):
    #파이썬은 zero-base이기 때문에, k+1만큼 수를 셀 리스트를 만들어줌
    counting_arr = [0] * (k+1)
    #input_arr의 리스트 인덱스를 순회하며
    #input_arr의 인덱스에 있는 수를 counting_arr 인덱스로 지정하고, 개수를 1 더해줌
    for i in range(0, len(input_arr)) :
        counting_arr[input_arr[i]] +=1
    # counting_arr를 1부터 순회하며, 그 전 값에 1을 더해줌
    #즉 [0,0,2,2,3,4]로 리스트가 형성되면,
    #0 없음 1 없음 2가 1~2, 3 없음 4 3 5 4
    #0 없음 1 없음 2가 2개, 3 없음 4가 1개 5가 1개
    for i in range(1 , len(counting_arr)) :
        counting_arr[i] += counting_arr[i-1]
    # 결과가 담길 리스트 초기화
    result_arr = [-1] * len(input_arr)

    #input_arr의 값을 index로 가져옵니다. 이를 사용하여 counting_arr에 들어있는 해당 값이 들어갈 수 있는 가장 오른쪽 index를 찾습니다.
    #input_arr의 i번째에 해당하는 값을 찾아 그 수를
    for i in range(len(result_arr) - 1, -1, -1) :
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]


    return result_arr
#정렬할 숫자가 담긴 리스트와 숫자의 범위의 마지막 값을 입력
#ex) 1~9 범위면 9로
print(counting_sort([2,4,5,2],5))