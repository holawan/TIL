# ______________________________________________________________________________


# 정수 하나 입력받기
# 5

# n = int(input())


# ______________________________________________________________________________


# 띄어쓰기로 구분된 여러 정수를 리스트로 받기
# 1 2 3 4 5 6

# lst = list(map(int, input().split()))


# ______________________________________________________________________________


# 띄어쓰기로 구분된 여러 정수를 변수로 받기
# 1 2 3 4 5 6

# n, m = map(int, input().split())


# ______________________________________________________________________________


# 띄어쓰기로 구분되지 않은 정수를 변수로 받기
# 123456

# lst = list(map(int, input()))


# ______________________________________________________________________________


# 띄어쓰기로 구분된 문자 받기
# a b c d e f

# lst = input().split()


# ______________________________________________________________________________


# 2차원 리스트
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))


# ________________________________________


# n = int(input())
# lst = [list(map(int,input().split())) for _ in range(n)]


# ______________________________________________________________________________


# 세로 m칸, 가로 n칸 grid 만들기 grid: 0으로 이루어진 2차원 리스트

# n = 3
# m = 4

# lst = [[0]*n for _ in range(m)]

# ________________________________________

# n = 3
# m = 4

# lst = []
# for _ in range(m):
#     lst.append([0]*n)


# ______________________________________________________________________________


# local에서 txt파일로 인풋 받기 ( 실행 파일과 같은 디렉토리 내에 input.txt가 존재할 때)

# import sys
#
# sys.stdin = open("input.txt")


