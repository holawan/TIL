T = int(input())

for t in range(1,T+1) :
    #N은 행의 개수 #K는 구간
    n, k = map(int,input().split())

    #n행만큼 값을 불러온 후 2차원 리스트 생성하기
    grid = [list(map(int,input().split())) for _ in range(n)]

    #구간 합들을 담을 result 배열 만들기
    result = []

    #행의 길이n만큼 순회하며
    for row in range(n) :
        #행별 구간합을 담을 x변수 만들기
        x= 0

        #열을 행의 인덱스부터 인덱스+k-1 까지 순회
        for column in range(row,row+k) :

            #열이 리스트의 범위를 초과하지 않으면 구간합에 +하기
            if column < n:
                x += grid[row][column]

            #열이 리스트의 범위를 초과하면 반복문 멈추기
            else :
                break

        #구간합을 구간합 배열에 추가
        result.append(x)
    #구간합 최대값은 구간합배열의 첫번째값
    subset_max = result[0]

    #구간합 배열을 순회하며
    for num in result :
        #해당 수가 구간합 최대값보다 크면

        if num > subset_max :
            #구간합 최대값 갱신
            subset_max = num

    #테스트 케이스와 구간합 리턴
    print(f'#{t} {subset_max}')