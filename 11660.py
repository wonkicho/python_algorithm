n, m = map(int, input().split())

"""
Arr = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    Arr.append(temp)

for _ in range(m):
    x1, y1, x2 ,y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1 , y2 - 1
    s = 0
    
    for i in range(x1, x2 + 1):
        for j in range(y1 , y2 + 1):
            s += Arr[i][j]
            
    print(s)
"""

Arr = []
D = [[0 for i in range(n + 1)] for i in range(n + 1)]
print(D)
for i in range(n):
    temp = [int(x) for x in input().split()]
    Arr.append(temp)
    
    
for i in range(n):
    for j in range(n):
        
        D[i+1][j+1] = D[i][j+1] + D[i+1][j] - D[i][j] + Arr[i][j]
        
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] - (D[x1 - 1][y2] + D[x2][y1 - 1] - D[x1 - 1][y1 - 1]))