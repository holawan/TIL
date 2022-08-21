# T : target / P : pattern


def pre_process(P):
    from collections import defaultdict

    M = len(P)    

    # skip 배열 대신 딕셔너리
    PI = defaultdict(int)

    # 실 사용은 M - value로 할 예정.
    for i in range(M):
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