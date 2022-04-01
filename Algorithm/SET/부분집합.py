def f(i, r):
    if i==r: 
        print(bit)
        return
    else:
        bit[i] = 0
        f(i+1,r)
        bit[i] = 1
        f(i+1,r)
    return


N = 4
lst = list(range(1,N))
bit = [0]*N
f(0, N)