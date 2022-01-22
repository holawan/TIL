data = input()

lst1 = []
lst2 = []
num = ''

for i in data : 
    if i in ['+','-'] :
        lst1.append(int(num))
        lst1.append(i)
        num = ''
    else: 
        num += i
lst1.append(int(num))

s= [0]
for i in range(len(lst1)) :
    if lst1[i] == '-' :
        s.append(i)
result = []
print(s)
for i in range(len(s)-1) :
    result.append(lst1[s[i]:s[i+1]:2])
# for i in s :
#     result.append(sum(lst1[i:i+1:1]))


#for i in range(lst1[i]) :
    
# for i in range(len(lst1)) : 
#     if lst1[i] == '-' :
#         break
#     else : 
#         i = None
# cal = [lst2[0],0]

# k = 0

# print(cal)
# print(i)
# for j in range(len(lst1)) :
#     if j == i :
#         k += 1
#         cal[k] = lst2[j+1]
#     else :
#         if lst1[j] == '+' :
#             cal[k] += lst2[j+1]
#         else :
#             cal[k] -= lst2[j+1]
#     print(cal)
# print(cal)
# print(cal[0]-cal[1])
