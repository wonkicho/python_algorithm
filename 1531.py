n, m = map(int, input().split())

board = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            board[x-1][y-1] += 1


result = 0        
for i in range(100):
    for j in range(100):
        if board[i][j] > m:
            result += 1
            
print(result)