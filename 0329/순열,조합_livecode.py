# 순열

def perm( n,  k ): # p[n]을 채워서 k개의 숫자로 만드는 순열, 인덱스가 사전순으로 생성
    if n == k:
        print(p)
    else:
        for i in range(k):		# 모든 원소에 대해
            if used[i] == 0:    # 사용된 적이 없으면
                p[n] = arr[i]	# 순열에 사용
                used[i] = 1 	# 사용됨으로 표시
                perm(n+1, k)
                used[i] = 0	# 다른 자리에서 사용가능

arr = [1,2,3]
p = [0]*3
used = [0]*3
perm(0, 3)

def f(n, k, m):    # 순열 p[n]을 채우는 함수. k 고를 개수, m 주어진 숫자 개수
    if n==k:
        print(p)
    else:
        for i in range(m): # used에서 사용하지 않은 숫자 검색
            if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1     # 사용함으로 표시
                p[n] = a[i]     # p[n] 결정
                f(n+1, k, m)
                used[i] = 0     # a[i]를 다른 위치에서 사용할 수 있도록 함
    return

a = [1,2,3,4,5]
p = [0]*3
used = [0]*5
f(0, 3, 5)


# 조합
def nCr(n, r, s):   # n개에서 r개를 고르는 조합. s 고를 수 있는 구간의 시작 인덱스
    if r==0:
        print(comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

n = 5
r = 3
comb = [0]*3
A = [i for i in range(1, n+1)]
nCr(n, r, 0)


def nCr(n, r, s, k):   # n개에서 r개를 고르는 조합. s 고를 수 있는 구간의 시작 인덱스
    if r==0:
        print(comb)
    else:
        for i in range(s, n-r+1):
            comb[k-r] = A[i]
            nCr(n, r-1, i+1, k)

n = 10
r = 3
k = r
comb = [0]*r
A = [i for i in range(1, n+1)]
nCr(n, r, 0, k)