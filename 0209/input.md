## input

### input이 있으면, input부터 잘 되었는지 확인하고 로직을 시작하자 !! 

``` python
#정수 1개를 입력받을 때
n = int(input()) 
#string 1개를 입력 받을 때
s = input()
#띄어쓰기가 된 여러개의 값을 입력받을 때
s = input().split()
#띄어쓰기로 구분되지 않은 정수를 변수로 받기
lst = list(map(int,input()))
#정수 여러개를 입력받을 때 
lst = list(map(int,input().split()))

#각 변수에 입력값을 받을 때
n,m = map(int,input().split())

# n만큼 값을 불러와야할 때 
'''
3
1 2 3 
4 5 6
7 8 9
'''
## 1. 
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
## 2. 
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

# 그리드 만들기 
lst = [[0]*3*4] # 얕은 복사
# 
n,m=3,4
lst = [[0]*n for _ in range(m)]
```

