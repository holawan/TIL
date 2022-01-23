# data = input() 

# unique = ['lj','nj','dz','=','-'] 

# k = 0
# for i in data :
#     k += 1 
#     if i in unique[3:5] :
#         k -= 1
# l = len(data)
# for i in range(1,l) :
#     if data[i-1:i+1] in unique[0:3] : 
#         k -= 1
# print(k)


data = input() 

unique = ['lj','nj','c=','c-','d-','s=','z=','dz='] 

l = len(data)

for i in range(1,l) :
    if data[i-1:i+1] in unique[0:7] :
        l -= 1 
    if data[i-1:i+2] == unique[7] :
        l -= 1 

        
print(l)
