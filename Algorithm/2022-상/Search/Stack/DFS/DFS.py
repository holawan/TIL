input_str = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"


lst = list(map(int,input_str.split(", ")))
grid = [[0]*8 for _ in range(8)]
# 1
from collections import defaultdict

# 그래프 만들기
graph = defaultdict(list)
for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i+1]


    
    grid[a][b] = 1
    grid[b][a] = 1

    graph[a].append(b)
    graph[b].append(a)
    
from pprint import pprint

# pprint(grid)
# pprint(graph)


stack = []
visited = []
print(i)

stack.append(1)
visited.append(1)

while stack:

    tmp = stack[-1]


    for node in range(1,8): # 7 : node의 개수 1 ~ 7
        if grid[tmp][node] == 1 and node not in visited:
            stack.append(node)
            visited.append(node)
            break
    else:
        stack.pop()


    # for value in graph[tmp]:
    #     if value not in visited:
    #         stack.append(value)
    #         visited.append(value)
    #         break
    # else:
    #     stack.pop()
    
print(visited)


# for i in range(0, len(lst), 2):
#     print(i, i+1)

# for i in range(len(lst)//2):
#     print(2*i, 2*i+1)    

# for i in range(len(lst)):
#     if i%2:
#         print(i-1, i)

# for i in range(len(lst)):
#     if i%2 == 0:
#         print(i, i+1) 