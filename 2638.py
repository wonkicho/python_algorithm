from collections import deque


n, m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0,0])
    visited = [[0]*m for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == 0:
                #치즈가 존재한다면
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                
                else:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

result = 0
while True:
    bfs()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                cnt = 1

            elif graph[i][j] == 2:
                graph[i][j] = 1

    if cnt == 1:
        result += 1
    else:
        break

print(result)

