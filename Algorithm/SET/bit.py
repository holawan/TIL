# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2) :
#         bit[1] = j
#         for k in range(2) :
#             bit[2] = k
#             for l in range(2) :
#                 bit[3] = k
#
# # 비트 연산자
#

#
# for i in range(1<<n) :
#     for j in range(n) :
#         if i & (1<<j) :
#             print(arr[j], end = ", ")
#     print()

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

#
# arr = [1, 2, 3]
# subsets = [[]]
# for num in arr:
#   size = len(subsets)
#   for y in range(size):
#     subsets.append(subsets[y]+[num])
# print(subsets)