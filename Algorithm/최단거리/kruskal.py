



'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

V, E = map(int,input().split())
graph_kruskal = [list(map(int,input().split())) for _ in range(E)]

parent = [-1]*(V+1)
rank = [-1]*(V+1)   


def make_set(x):
    parent[x] = x
    rank[x] = 0

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union(x,y):
    link(find_set(x), find_set(y))

def link(x,y):
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def mst_kruskal():

    mst = []

    for i in range(V+1):
        make_set(i)

    graph = sorted(graph_kruskal, key=lambda x : x[2])

    while len(mst) < V and graph:
        s, e, weight = graph.pop(0)
        if find_set(s) != find_set(e):
            mst.append((weight,s,e))
            union(s,e)
    print(mst)
    return sum(map(lambda x : x[0], mst))

print(mst_kruskal())