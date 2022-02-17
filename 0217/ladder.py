import sys

sys.stdin = open('input.txt')

# 좌 우 상
dx = [0, 0, -1]
dy = [-1, 1, 0]


def search(x, y):

    # 출발점에 도착할 때까지
    # while x != 0:
    while x > 0 :
        # 왼쪽, 오른쪽, 위 순서대로 찾기
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            # nx, ny가 그리드 안에 있고 새로운 자리가 길이면 
            if 0<=nx<100 and 0<=ny<100 and data[nx][ny] == 1:
                # 이전 자리 0으로 변경, x, y 갱신
                data[nx][ny] = 0
                x = nx
                y = ny
    return y


for tc in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    # 출발점이 아닌 도착점에서 시작. search함수는 결과적으로 1번만 실행.
    for i in range(100):
        if data[99][i] == 2:

            result = search(99, i)
            break

    print(f'#{tc} {result}')