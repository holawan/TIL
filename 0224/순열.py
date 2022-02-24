def f(i, r):
    if i==r: 
        print(bit[:r])
        return
    else:
        for n in range(4):
            if n not in bit[0:i]:
                bit[i] = n
                f(i+1,r)
    return


N = 4
lst = list(range(1,N))
bit = [0]*N
f(0, N-1)