import sys
sys.setrecursionlimit(10000)

def dfs(start):

    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False] * (1+n)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)