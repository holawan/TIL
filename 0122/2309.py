import random as random
a = list(int(input()) for _ in range(9))
#print(a)

result = 0
while result !=100 : 
    c = random.sample(a,7)
    result = sum(c)

c = sorted(c)

for i in c:
    print(i)