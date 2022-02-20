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



## 이진탐색

```python
def binary_search(lst,target) :
    length = len(lst)
    start = 0
    end = lenght-1 #끝 쪽수
    while start<=end : #찾으려는 부분 처음이 끝보다 작거나 같으면
        middle = (start+end)//2 #middle start+end를 2로 나눈 값의 몫
        if target == middle : #target과 middle이 같으면
            return cnt #반복 횟수 반환
        elif middle > target : #middle이 찾으려는 target보다 크면
            end = middle-1 #마지막 부분 -1을 middle로 갱신
        else : #middle이 찾으려는 target보다 작으면
             start = middle+1 #처음 부분 +1을 middle로 갱신
    return False
```

1.  시작점과 끝점을 지정한다.
2. 시작점이 끝점보다 작거나 같으면
3. 중앙은 (시작점+끝점)을 2로 나눈 몫
4. 찾으려는 값과 일치하면
   1. 끝냄
5. 일치하지 않고 중앙값이 찾으려는 값보다 크면 
   1. 끝점을 middle-1
6. 중앙값이 찾으려는 값보다 작으면 
   1. 시작점을 middle+1로

## BruteForce

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
