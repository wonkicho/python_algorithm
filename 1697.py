import sys
from collections import deque


input = sys.stdin.readline()

def bfs():
    queue = deque()
    queue.append(s)

    while queue:
        point = queue.popleft()

        if point == e:
            print(mem[point])
            break

        for nx in (point-1, point+1, point*2): 
            if (0 <= nx <= MAX) and (not mem[nx]):
                mem[nx] = mem[point] + 1
                queue.append(nx)
        
        
MAX = 10 ** 5
s, e = map(int, input.split())
mem = [0] * (MAX + 1)
bfs()
