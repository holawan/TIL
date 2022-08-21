# s1 = list(input())
# s2 = input()
# print(s1)
# print(s2)
# # s1[0] = 'd'
# #에러, string은 immutable
# print(s1[0])
# print(s2[0])

# # strlen 함수 만들어보기
# def mystrlen(s) :
#     i = 0
#     while s[i]!='\0' :
#         i+=1
#     return i
# a = ['a','b','c','d','\0']
# print(mystrlen(a))


# a = ['a','b','c','d','\0']
# # print('a', end = '')
# # print('\n',end='')
# # print('b')
#
# print('a\nb')

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# print(s1==s2,s1 is s2 ,s1==s4, s1 is s4, s2 == s4, s2 is s4, s1 == s5 ,s1 is s5)


# n = int(input())
#
# for i in range(n) :
#     s = input()
#     print(s[::-1])


def itoa(s) :
    i = 0
    for x in s :
        i = i*10 + ord(x)-ord('0')
        print(i)
    return i
#
# n = int(input())
# for i in range(n) :
#     S = input()
#     itoa(S)
# print(ord('-'))
# print(ord('0'))
# print(ord('3'))

#p : pattern
#t : text
def BruteForce(p,t):
    i = 0
    j = 0

    while i+j <len(t) :
        if t[i+j] != p[j] :
            i += 1
            j = 0
        else :
            j += 1
        if j == len(p) :
            return 1

    return -1

def BruteForce2(p,t) :
    i = 0
    j = 0

    for i in range(n-m + 1) :
        for j in range(m) :
            if t[i+j] != p[j]:
                break
        else :
            return i #성공

    return 0



def kmp(t,p) :
    N = len(t)
    M = len(p)
    lps = [0]*(M+1)
    #preprocessing
    j= 0 #일치한 개수 == 비교할 패턴 위치
    lps[0] = -1

    for i in range(1,M) :
        lps[i] = j
        if p[i] == p[j] :
            j +=1
        else :
            j = 0

    lps[M] = j
    i = 0   #비교할 위치
    j = 0    #비교할 패턴 위치
    while i< N and j<=M :
        if j== -1 or t[i] == p[j] : #첫글자가 불일치했거나, 일치하면
            i +=1
            j+=1
        else :      #불일치
            j = lps[j]
        if j==M :    #패턴이 맞을 경우
            print(i-M, end=' ')
            j = lps[j]


