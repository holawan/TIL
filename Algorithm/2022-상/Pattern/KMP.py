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