lst = [1, 2, 3, 4, 5]
div = '#'*30
r = 3

# 순열
def make_perm(perm):
    if len(perm) == r:
        print(perm)
        return
    for i in lst:
        if i not in perm:
            perm.append(i)
            make_perm(perm)
            perm.pop()

print(div, '순열', div)
make_perm([])

# 중복순열
def make_perm_re(perm):
    if len(perm) == r:
        print(perm)
        return
    for i in lst:
        # if i not in perm:
        perm.append(i)
        make_perm_re(perm)
        perm.pop()

print(div, '중복순열', div)
make_perm_re([])


# 조합 / sort 된 상태에서
def make_combi(combi):

    if len(combi) == r:
        print(combi)
        return


    for i in lst:
        if combi and i <= max(combi):
            continue
        combi.append(i)
        make_combi(combi)
        combi.pop()

print(div, '조합', div)
make_combi([])



# 조합
def make_combi_2(combi, idx):

    if len(combi) == r:
        print(combi)
        return

    for i in range(idx+1, len(lst)):
        combi.append(lst[i])
        make_combi_2(combi, i)
        combi.pop()


print(div, '조합', div)
make_combi_2([], -1)


# 중복조합 / sort 된 상태에서
def make_combi_re(combi):

    if len(combi) == r:
        print(combi)
        return


    for i in lst:
        if combi and i < max(combi):
            continue
        combi.append(i)
        make_combi_re(combi)
        combi.pop()

print(div, '중복조합', div)
make_combi_re([])        



# 중복조합
def make_combi_2_re(combi, idx):

    if len(combi) == r:
        print(combi)
        return

    for i in range(idx, len(lst)):
        combi.append(lst[i])
        make_combi_2_re(combi, i)
        combi.pop()


print(div, '중복조합', div)
make_combi_2_re([], 0)    