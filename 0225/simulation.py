my_chu = 20 


next_person = 1
q = []

q.append([1,1])

while my_chu > 0 :
    num,cnt = q.pop(0)
    my_chu -= cnt 

    q.append([num,cnt+1])
    q.append([next_person + 1 ,1])
    print(f'q : {q} my_chu : {my_chu}')