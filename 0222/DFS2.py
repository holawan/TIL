input_str = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"


lst = list(map(int,input_str.split(", ")))


# 2칸씩 띄워서 index 가져오기
for i in range(0, len(lst), 2):
    print(i, i+1)

for i in range(len(lst)//2):
    print(2*i, 2*i+1)    

for i in range(len(lst)):
    if i%2:
        print(i-1, i)

for i in range(len(lst)):
    if i%2 == 0:
        print(i, i+1) 

# 그래프 만들기 - 2차원 리스트
grid = [[0]*8 for _ in range(8)]
for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]    
    grid[a][b] = 1
    grid[b][a] = 1


# 그래프 만들기 - 딕셔너리
from collections import defaultdict
graph = defaultdict(list)

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]    
    graph[a].append(b)
    graph[b].append(a)
    
from pprint import pprint

pprint(grid)
pprint(graph)

# dfs, 2차원 리스트
# stack : 근처에 방문할 수 있는 node가 있을 가능성이 있는 node / 근처의 모든 node를 방문했으면 pop
stack = []
# visited : 방문표시
visited = []

# 1에서 시작
stack.append(1)
visited.append(1)

# 모든 node에 대한 가능성을 확인할때까지
while stack:

    # stack의 top의 값 확인(peek)
    tmp = stack[-1]

    # 모든 노드에 대해
    for node in range(1,8): # 7 : node의 개수 1 ~ 7
        # 인접해있고(간선으로 연결되어 있고) and 방문하지 않았으면
        if grid[tmp][node] == 1 and node not in visited:
            # stack 및 visited에 append.
            stack.append(node)
            visited.append(node)
            # break가 없다면 탐색은 가능하지만, DFS는 아님
            break
    # 해당 노드와 연결된 모든 노드에 방문하였으면 stack에서 제외
    else:
        stack.pop()
print(visited)


# dfs, 딕셔너리
# stack : 근처에 방문할 수 있는 node가 있을 가능성이 있는 node / 근처의 모든 node를 방문했으면 pop
stack = []
# visited : 방문표시
visited = []

# 1에서 시작
stack.append(1)
visited.append(1)

# 모든 node에 대한 가능성을 확인할때까지
while stack:

    # stack의 top의 값 확인(peek)
    tmp = stack[-1]

    # tmp와 연결되어있는 node에 대해
    for node in graph[tmp]:
        # 방문하지 않았으면
        if node not in visited:
            # stack 및 visited에 append.
            stack.append(node)
            visited.append(node)
            # break가 없다면 탐색은 가능하지만, DFS는 아님
            break
    # 해당 노드와 연결된 모든 노드에 방문하였으면 stack에서 제외
    else:
        stack.pop()
    
print(visited)
