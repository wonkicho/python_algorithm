graph = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]


def dfs(i, j):
    if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]) or graph[i][j]!='1':
        return
    
    graph[i][j] = 0
    # 동서남북
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

counts = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '1':
            dfs(i, j)
            counts += 1
            
print(counts)
