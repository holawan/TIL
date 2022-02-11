


def bubble_sort(num):


    # 3. 오른쪽 끝을 나타내는 i가 n-1 ~ 1 까지 이동합니다
    for i in range(len(num) - 1, 0, -1):

        # 1. index j가 0부터 i까지 이동하면서
        for j in range(0, i):

            # 2. num의 j번째 원소가 바로 오른쪽 원소보다 크면 위치를 바꿉니다
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

    return num


num = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(bubble_sort(num))