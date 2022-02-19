'''
3
1 2 3
4 5 6
7 8 9
'''
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
#
'''
3
123
456
789
'''
# N= int(input())
# arr = [list(map(int,input())) for _ in range(N)]
# print(arr)


# #복사가 되는 경우
# arr = [[0]*3]*4
# print(arr)
# arr[0][1] = 1
# print(arr)
# n = 5
# m=5
# Array = [list(j for j in range(m))for i in range(n)]
# #행 우선 순회
# #i 행의 좌표
# #j열의 좌표
# for i in range(n) :
#     for j in range(m) :
#         print(Array[i][j])
#
# #열 우선 순회
# for j in range(m) :
#     for i in range(n):
#         print(Array[i][j])
#
# #지그재그 순회
# for i in range(n) :
#     for j in range(m):
#         Array[i][j+(m-1-2*j)*(i%2)]
# ##
# for i in range(n):
#     if i%2 :
#         for j in range(m-1,-1,-1):
#             print(Array[i][j])
#     else :
#         for j in range(m):
#             print(Array[i][j])
# from pprint import pprint
# # 0 앞뒤로 붙이기
# N = int(input())
# #arr1 = [0]+list(map(int,input().split()))+[0]
# arr2 = [[0]*(N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
# pprint(arr2)

#델타를 이용한 2차 배열 탐색
arr = [[1,2,3],[4,5,6],[7,8,9]]
N = 3
for i in range(N) :
    for j in range(N) :
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] :
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                print(i,j,arr[ni][nj])
        print()

# di = [0, 1, 0, -1] #우하좌상
# dj = [1,0, -1, 0]
# for k in range(4) :
#     ni = i + di[k]
#     nj = j + dj[k]
#     if 0<=ni<N and 0<=nj<M :
#         arr[ni][nj]
#
# for di,dj in [(0,1),(1,0)],(0,-1),(-1,0)] :
#     ni = i+ di
#     nj = j + dj
#     if 0<=ni<N and 0 <=nj<M :
#         arr[ni][nj]