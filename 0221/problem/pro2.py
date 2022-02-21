T = int(input())
for t in range(1,T+1) :
    #N은 행/열의 길이
    n = int(input())

    #그리드 만들기
    grid = [list(map(int,input().split())) for _ in range(n)]

    #영역의합을 담을 배열
    result = []

    # 3x3 배열
    for i in range(n) :
        for j in range(n) :
            #범위 벗어나는지 확인할 x
            x = 0
            #인덱스가 벗어날 수 있는 수들
            out_idx = [i-1,j-1,i+1,j+1]
            for k in out_idx :
                #out_idx가 인덱스를 벗어나면
                if k <0 or k>=n :
                    #x를 -1로 선언
                    x = -1
                    break
                #x가 -1이면
            if x == -1 :
                #결과에 0을 append
                result.append(0)
                continue
            #아니면 행을 -1범위부터 +1 범위까지 j-1부터 j+1까지 더한 값을 thr_sum으로 선언함
            else :
                thr_sum = 0
                for thr in range(-1,2,1) :
                    thr_sum += sum(grid[i-thr][j-1:j+2])

            #결과에 추가
            result.append(thr_sum)

    #n방향 원소합
    for i in range(n):
        for j in range(n):
            #원소가 1이면 1을 결과에 추가
            if grid[i][j] == 1 :
                result.append(1)
            #원소가 1이 아니면
            else :
                #방향마다 계산을 해야하기 때문에 grid[i][j]-1
                direction = grid[i][j]-1
                #탐색을 할 범위 지정을 위해 i와 j에 연산을 해서 구간을 정해줌
                start_row = i-direction ; start_column = j-direction
                end_row = i+direction ; end_column = j+direction
                #구간 계산 값이 인덱스 범위를 벗어나면 범위 안에 들어오도록 조정함
                if start_row <= 0 :
                    start_row = 0
                if start_column <= 0 :
                    start_column = 0
                if end_row >= n :
                    end_row = n-1
                if end_column >= n :
                    end_column = n-1
                #겹치는 지점을 빼주기 위해 cross값을 -grid[i][j]로 시작
                cross = -grid[i][j]
                #열을 고정시키고 행을 순회하며 cross에 더해줌
                for row in range(start_row,end_row+1) :
                    cross = cross + grid[row][j]
                #행을 고정시키고 열을 순회하며 cross에 더해줌
                for column in range(start_column,end_column+1) :
                    cross = cross + grid[i][column]
                result.append(cross)
    print(result)
    my_max = result[0]
    # 결과값을 순회하며
    for num in result:
        # 해당 수가 결과의 최대값이면

        if num > my_max:
            #  최대값 갱신
            my_max = num

    # 테스트 케이스와 최대값 리턴
    print(f'#{t} {my_max}')