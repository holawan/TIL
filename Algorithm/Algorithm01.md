## 2차원 배열 기본 

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



## 비트연산자 완전탐색

``` python
#부분집합의 모든 경우를 순회하며
power_set = []
n = 3
arr = [i+1 for i in range(n)]
print(arr)
for i in range(1<<n) : #1부터 12까지를 원소로 가지는 집합의 부분집합의 수는 2의 12승
    tmp_set = [] #부분집합을 담을 임시저장소
    #n만큼 j가 순회하며
    for j in range(n) :
        #i의 j번째 비트가 1인지 아닌지 확인
        if i & (1<<j) :
            #for문을 순회하며 and연산 결과 True이면 A리스트의 j인덱스를 tmpset에 추가
            #ex 13이면 1101 이니까, 1,3,4번째 비트 추가
            tmp_set.append(arr[j])
    power_set.append(tmp_set)
print(power_set)

```

1. 부분집합의 모든 원소를 담을 power_set 준비해
2. 원래 집합 arr 준비해 
3. n은 arr의 길이 
4. 부분집합의 원소 합은 2^n이니까 1<<n만큼 순회해 
5. 부분집합을 담을 임시저장소 tmp_set준비해 
6. 그니까 부분집합의 원소가 2의 n승개니까 비트가 n-1개 있잖아 그걸 순회해 
7. i를 비트로 바꿨을 때 (예를들어 i가 13이면 1101) j도 1000,100,10,1 이런식으로 있을거란 말이야
8. 그럼 0번째 비트, 2번째 비트, 3번째 비트가 겹치잖아 그럼 그 j를 인덱스로 값을 arr배열에서 찾아서 임시저장소에 넣어 
9. 그연산이 종료되면 power_set에 넣어 

## 버블솔트

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 정렬 과정
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막자리까지 이동한다.
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다
  - 교환되면 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다. 
- 시간복잡도 : O(n^2)

```python
def bubble_sort(num):
    #원소의 마지막 부터
    #why? 최대값부터 마지막에 박고 오름차순으로 정렬할 것이기 때문
    for i in range(len(num)-1,0,-1) :
        #0번 index부터 i번째 index까지
        for j in range(0,i) :
            #num[j]가 num[j+1]보다 크면
            if num[j] > num[j+1] :
                #위치 변경
                num[j],num[j+1] = num[j+1],num[j]
    return num
num = [54,26,93,17,77,31,44,55,20]

print(bubble_sort(num))
```

1. 원소의 마지막부터 -1씩 후진하면서 시작해 최대값부터 마지막에 박을거야 
2. 0번째부터 i번째까지 왼쪽이 오른쪽보다 크면 자리 바꿔 
3. 그럼 마지막 값은 가장 큰 값으로 갱신되 
4. 그럼 이제 -2번째를 하는거야 
5. 계속 순환하면 정렬끝



## 카운팅솔트

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하며 선형 시간에 정렬하는 효율적인 알고리즘
- 제한사항
  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내 가장 큰 정수를 알아야한다. 
- 시간 복잡도 : O(n+k) :n은 리스트의 길이, k는 정수 최대값 
- 1단계 : Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장
- 2단계 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 원소를 조정  
- counts[i]를 감소시키고 temp에 삽입 

```python
def counting_sort(input_arr, k):
    # k : 0 ~ k

    # 원소들의 개수를 셀 빈 리스트를 만들어줍니다. 개수가 없을수도 있으니 0으로 초기화를 해줍니다.
    counting_arr = [0] * (k + 1)

    # 전체 리스트를 돌면서 개수를 세어줍니다.
    for i in range(len(input_arr)):
        counting_arr[input_arr[i]] += 1
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

    return result_arr

lst = [0, 4, 1, 3, 1, 2, 4, 1]

print(counting_sort(lst, 5)) # [0, 1, 1, 1, 2, 3, 4, 4]


```

1. 주어진 숫자의 범위만큼 카운팅배열을 만들어준다.
2. 전체 리스트를 돌면서 각 숫자의 개수를 세준다. 
3. 개수가 들어있는 카운팅 리스트가 순서를 가지도록 각 값에 이전 개수를 더해준다.
   - 예를들어 131120이면 
   - 145688
4. 결과를 담을 배열을 각 값을 -1로 지정한 후 만들어준다. 
5. 흐름을 변경하기 위해 input_arr을 뒤집어준다 (input_arr[::-1])
6. input_arr의 값을 index로 counting_arr에 들어있는 값을 -1한 후  (counting_arr[i])번째로  result_arr에 추가해줌

## 선택정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬 과정
  - 주어진 리스트 중에서 최소값을 찾는다. 
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
- 시간 복잡도 : O(n^2)

```python
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

1. 최소값을  i인덱스로 지정한다.
2. i+1부터 배열을 돌면서 최소인덱스를 찾는다.
3. 리스트의 맨 앞과 교환한다.
4. 미정렬 i가 증가함에 따라, 정렬된 부분과 미정렬된 부분이 나뉘어지고 계속 최소값을 찾아 미정렬 부분의 첫번째로 보낸다.

## 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격하게 증가하여 비효율적임
- 검색 과정
  - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 찾는다.
  - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
  - 자료구조의 마지막에 이를 때까지 검색대상을 찾지 못하면 검색을 종료한다. 
- 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
  - 첫번째 원소를 찾을때는 1번 비교, 두번째 원소를 찾을때는 2번 비교
  - 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
    -  (1/n)*(1+...+n) = (n+1)/2\
- 시간 복잡도 : O(n)

- 정렬되어 있는 경우
  - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교회수가 반으로 줄어든다.
  - 시간복잡도 : O(n)



```python
def sequentialSearch(lst,n,key):
    i = 0
    while i <n and a[i] !=key :
        i += 1 
    if i<n : 
        return i
   	else :
        return -1 
```

```python
def sequentialSearch2(lst,n,key) :
    i = 0
    while i<n and a[i]<key :
        i +=1 
    if i<n and a[i] == key:
        return i
   	else :
        return -1 
```



## 이진탐색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법 
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야함. 
- 검색 과정
  - 자료의 중앙에 있는 원소를 고른다.
  - 중앙 원소의 값과 찾고자하는 목표값을 비교한다.
  - 목표값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다. 
  - 

```python
def binary_search(lst,target) :
    length = len(lst)
    start = 0
    end = lenght-1 #끝 쪽수
    while start<=end : #찾으려는 부분 처음이 끝보다 작거나 같으면
        middle = (start+end)//2 #middle start+end를 2로 나눈 값의 몫
        if target == lst[middle] : #target과 middle이 같으면
            return cnt #반복 횟수 반환
        elif lst[middle] > target : #middle이 찾으려는 target보다 크면
            end = middle-1 #마지막 부분 -1을 middle로 갱신
        else : #middle이 찾으려는 target보다 작으면
             start = middle+1 #처음 부분 +1을 middle로 갱신
    return False
```

1.  시작점과 끝점을 지정한다.
2.  시작점이 끝점보다 작거나 같으면
3.  중앙은 (시작점+끝점)을 2로 나눈 몫
4. 찾으려는 값과 일치하면
   1. 끝냄
5. 일치하지 않고 중앙값이 찾으려는 값보다 크면 
   1. 끝점을 middle-1
6. 중앙값이 찾으려는 값보다 작으면 
   1. 시작점을 middle+1로

- 재귀함수 이용

```python
def binarySearch2(a,low,high,key) :
    if low>high :
        return False 
    else :
        middle = (low+high)//2
        if key == a[middle] : 
            return True
        elif key < a[middle] :
            return binarySearch2(a,low,middle-1,key)
        elif a[middle]<key :
            return binarySearch2(a,middle+1,high,key)
```



## BruteForce

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작 
- 최악의 경우 시간복잡도는 텍스트의 모든 위치에서 패턴을 비교해야하므로 O(MN)이 됨

```python
def BruteForce2(p,t) :
    n = len(t)
    m = len(t)
    cnt = 0
    for i in range(n-m + 1) :
        match = 0
        for j in range(m) :
            if t[i+j] != p[j]:
                break
            else :
                match +=1
        if match == m :
            cnt += 1

    return cnt
```

1. 길이-패턴 +1만큼 (인덱스 에러 방지)
2. 패턴을 돌며 텍스트의 i+j번째가 패턴의 j번째와 다르면 for문 멈춤 
3. 일치하면 계속 
4. j가 m-1과 같으면 
5. 일치하는 것으로 간주 

## KMP

- 불일치가 발생한 텍스트 스트링의 앞부분에 어떤 문자가 있는지를 미리 일고 있으므로, 불일치가 발생한 앞부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴에 중복이 있을 경우에만 적용 가능 
- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함
- 시간복잡도: O(M+N)
- 텍스트에서 abcdabc까지는 매치되고 e에서 실패한 상황 패턴의 맨 앞의 abc와 실패직전의 abc는 동일함을 이용

```python
# T : target / P : pattern

def pre_process(P):

    M = len(P)
    lps = [0] * len(P)
    
    j = 0

    for i in range(1,M):
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1  

    return lps


def KMP(T, P, lps):

    N = len(T)
    M = len(P)

    i, j = 0, 0
    pos = -1
    while i < N:
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            if j!= 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            pos = i - j
            break

    return pos

T = 'abcdabeeababcdabcef'
P = 'abcdabcef'


N = len(T)
M = len(P)
lps = pre_process(P)
print(lps)

pos = KMP(T, P, lps)
print(pos)
```

## Boyer

- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 보이어-무어 알고리즘은 패턴에 오른쪽 끝에 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동거리는 무려 패턴의 길이만큼
- 앞의 두 매칭 알고리즘의 공통점 텍스트 문자열의 문자를 적어도 한번씩 훑는다.
- 보이어 무어 알고리즘은 텍스트 문자를 다 보지 않아도 됨
- 최악의 경우 수행시간 O(MN)
- 입력에 다라 다르지만 일반적으로 O(n) 보다 시간이 덜 소요됨 

```python
# T : target / P : pattern


def pre_process(P):
    from collections import defaultdict

    M = len(P)    

    # skip 배열 대신 딕셔너리
    PI = defaultdict(int)

    # 실 사용은 M - value로 할 예정.
    for i in range(M-1):
        PI[P[i]] = 1 + i
    return PI


def boyer_moore(T, P, PI):

    N = len(T)
    M = len(P)

    i = 0
    # 실패할 경우 -1 return
    pos = -1

    while i <= N - M:
        # skip 잘 되고있나 확인
        print(i)

        # 
        # M번째 인덱스
        j = M - 1
        k = i + M - 1

        # 비교할 j가 남아있고, text와 pattern이 같으면 1씩 줄여 왼쪽 비교
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1
        # 비교 성공
        if j == -1:
            pos = i
            break
        # i를 M - value만큼 스킵
        i = i + M - PI[T[i + M - 1]]

    return pos




# Target 문자
T = "a pattern matching algorithm"

# Pattern 문자
P = "rithm"

# skip 배열을 만들어줌
PI = pre_process(P)
print(PI)

# target, pattern, skip배열을 인자로 넘김
pos = boyer_moore(T, P, PI)
print(pos)
```

```python
#BoyerMooer algorithm
#불필요한 탐색 스킵
def skip(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern)-i-1
    return len(pattern)
#BM 본 함수
#text안에 pattern과 일치하는 문자열 있으면 1반환 바로 종료
#끝까지 탐색했는데 pattern과 일치하는 문자열이 없으면 0반환
def boyer(pattern, text):
    cnt = 0
    patternlen = len(pattern)
    textlen = len(text)
    i = 0
    while i <= textlen - patternlen:
        j = patternlen - 1
        while j >= 0:
            if pattern[j] != text[i+j]:
                move = skip(pattern, text[i + patternlen - 1])
                break
            j = j - 1
        if j == -1:
            cnt += 1
            return 1
        else:
            i += move
    return 0
```

