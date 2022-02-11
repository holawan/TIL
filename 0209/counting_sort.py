


def counting_sort(input_arr, k):
    # k : 0 ~ k

    # 원소들의 개수를 셀 빈 리스트를 만들어줍니다. 개수가 없을수도 있으니 0으로 초기화를 해줍니다.
    counting_arr = [0] * (k + 1)




    # 전체 리스트를 돌면서 개수를 세어줍니다.
    for i in range(len(input_arr)):
        counting_arr[input_arr[i]] += 1

    # 13 ~ 15번째 코드와 같은 코드입니다.
    # for num in input_arr:
    #     counting_arr[num] += 1


    # 개수가 들어있는 counting array를 input_array의 원소들의 인덱스를 바라볼 수 있도록 변경해줍니다.
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    # 결과가 담길 리스트를 초기화해줍니다. 0~k가 아닌 값으로 초기화해주는게 오류를 확인하기 좋습니다
    result_arr = [-1] * len(input_arr)


    # 오른쪽 -> 왼쪽의 흐름을 왼쪽 -> 오른쪽 흐름으로 가져오기 위해 리스트를 뒤집어줍니다.
    input_arr = input_arr[::-1]

    # input_arr의 값을 index로 가져옵니다. 이를 사용하여 counting_arr에 들어있는 해당 값이 들어갈 수 있는 가장 오른쪽 index를 찾습니다.
    # counting_arr의 숫자는 1부터 시작하는 "번째"의 개념이고, 파이썬은 0부터 시작하기 때문에 -1을 하여 값을 맞추어줍니다.
    # -1을 한 값에 맨 처음 가져온 input_arr의 값을 넣어줍니다.
    for i in input_arr:
        counting_arr[i] -= 1
        result_arr[counting_arr[i]] = i

    # {위 코드의 i} == {해당 코드의 input_arr[i]}입니다. 왜인지 생각해보세요!
    # for i in range(len(input_arr) - 1, -1, -1):
    #     counting_arr[input_arr[i]] -= 1
    #     result_arr[counting_arr[input_arr[i]]] = input_arr[i]

    return result_arr


lst = [0, 4, 1, 3, 1, 2, 4, 1]

print(counting_sort(lst, 5)) # [0, 1, 1, 1, 2, 3, 4, 4]

