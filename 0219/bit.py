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


for i in range(1<<n) :
    tmp_set = []
    for j in range(n) :
        if i & (1<<j) :
            tmp_set.append(arr[j])
    power_set.append(tmp_set)
print(power_set)
print(sum([]))


arr = [1, 2, 3]
subsets = [[]]
for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])
print(subsets)