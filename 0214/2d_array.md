# 2차원 배열

### 2차원배열의 선언

- 1차원 LIst를 묶어놓은 list
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

``` ptyhon
arr = [[0,1,2,3],[4,5,6,7]]
```

| 0    | 1    | 2    | 3    |
| ---- | ---- | ---- | ---- |
| 4    | 5    | 6    | 7    |

```
3
1 2 3
4 5 6
7 8 9
```

``` python
N = int(input())
arr = [list(map(int,input().split())) for _in range(N)]
```

```
3
123
456
789
```

```python
N= int(input())
arr = [list(map(int,input())) for _in range(N)]
```

###  배열 순회

n x m배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

### 행 우선 순회

```python
# i행의 좌표
# j열의 좌표
for i in range(n) :
    for j in range(m) :
        Array[i][j]
```

### 델타를 이용한 2차 배열 탐색

```python
arr[0...N-1][0...N-1] # NxN배열
di[] <- [-1,1,0,0]
dj[] <- [0,0,-1,1]
# [-1,0]상 [1,0] 하 [0,-1] 좌 [0,1] 우
di = [0 1, 0, -1] #우하좌상
dj = [1,0, -1, 0]

# for k in range(4) :
#     ni = i + di[k]
#     nj = j + dj[k]
#     if 0<=ni<N and 0<=nj<M :
#         arr[ni][nj]
```



```python
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
```

### 0 앞뒤로 붙이기

```python
# 0 앞뒤로 붙이기
N = int(input())
#arr1 = [0]+list(map(int,input().split()))+[0]
arr2 = [[0]*(N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
pprint(arr2)
```

### 전치행렬

```python
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3) :
        if i < j :
            arr[i][j],arr[j][i]  = arr[j][i],arr[i][j]
```

### 비트 연산자

#### 10진수를 2진수로 변환후 연산을 진행하는 것 ?

- & : 비트 단위로 AND 연산을 한다.
- | : 비트 단위로 OR 연산을 한다.
- << :  피연산자의 비트 열을 왼쪽으로 이동시킨다. (X 2)
- \>> : 피연산자의 비트 열을 오른쪽으로 이동시킨다.  (// 2)

1 << n = 2^n 

​	즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
