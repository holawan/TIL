input_str = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"


lst = list(map(int,input_str.split(", ")))



grid = [[0]*8 for _ in range(8)]
for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]    
    grid[a][b] = 1
    grid[b][a] = 1


from collections import defaultdict
graph = defaultdict(list)

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]    
    graph[a].append(b)
    graph[b].append(a)
    
from pprint import pprint




stack = []
visited = []

stack.append(1)
visited.append(1)
cnt = 0
while stack:
    cnt += 1

    tmp = stack[-1]

    for node in graph[tmp]:
        if node not in visited:
            stack.append(node)
            visited.append(node)
            break
    else:
        stack.pop()
    
print(visited)
print(cnt)


visited = []

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]    
    graph[a].append(b)
    graph[b].append(a)


def func(tmp):
    visited.append(tmp)
    for node in graph[tmp]:
        if node not in visited:
            # visited.append(node)
            func(node)

func(1)
print(visited)
