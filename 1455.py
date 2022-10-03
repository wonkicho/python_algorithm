n, m = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def reverse(a, b):
    for r in range(a+1):
        for c in range(b+1):
            matrix[r][c] = 1 - matrix[r][c]

cnt = 0
for r in range(n-1 , -1, -1):
    for c in range(m-1, -1, -1):
        if matrix[r][c]:
            cnt += 1
            reverse(r,c)
            
            
            

print(cnt)