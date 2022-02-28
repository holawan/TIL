import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1) :
    n = int(input())
    #통로 = 0, 벽은 1, 경비원 = 2
    #상하좌우만 감시 가능
    #지도 가져오기
    grid = [list(map(int, input().split())) for _ in range(n)]
    #통로의 수
    gate = 0
    for r in range(n) :
        for c in range(n) :
            #경비원 위치 찾기
            if grid[r][c] == 2 :
                police = [r, c]
            #통로이면 gate에 1더함
            if grid[r][c] == 0 :
                gate +=1
#시계방향으로 탐색
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

#감시 가능한 통로 = cnt
    cnt = 0 #경비원 위치
#4방향을 돌며
    for i in range(4):
        # 초기 위치는 경비원 위치
        r, c = police[0], police[1]
        #새로운 위치는 방향에 +1한 값
        new_r = r + dr[i]
        new_c = c + dc[i]
        #범위 내에 있으며 벽이 아니면 +1
        while 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] != 1:
            cnt += 1
            new_r += dr[i]
            new_c += dc[i]
    print(f'#{t} {gate-cnt}')
