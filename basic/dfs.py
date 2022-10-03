discovered = []

graph = {
    1 : [2,3,4],
    2 : [5],
    3 : [5],
    4 : [] ,
    5 : [6, 7],
    6 : [],
    7 : [3],
}

def dfs(graph, v, discovered):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = dfs(graph, w, discovered)
    return discovered


print(dfs(graph, 1, discovered))