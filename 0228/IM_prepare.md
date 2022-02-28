# IM 대비 문제풀이



## 델타를 이용한 2차 배열 탐색

### A\[r]\[c] 주변의 4개 원소에 접근하는 방법

````python
dr = [0,1,0,-1]
dc = [1,0,-1,0]
tmp = 0 
for k in range(4) :
    nr,nc = r+ dr[k],c+dc[k]
    if 0<=nr<n and 0<=nc<n :
        tmp += grid[nr][nc]
    else :
        break
        
````

```python
dr = [0,1,0,-1]
dc = [1,0,-1,0]
tmp = 0 
for times in range(1,grid[r][c]+1)
    for k in range(4) :
        nr,nc = r+ dr[k]*times,c+dc[k]*times
        if 0<=nr<n and 0<=nc<n :
            tmp += grid[nr][nc]
        else :
            break
        
```



## 파리퇴치3

## 새로운 버스 노선

