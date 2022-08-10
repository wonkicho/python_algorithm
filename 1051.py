n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))
    
max_sq = min(n, m)

ans = 0

for i in range(n):
    for j in range(m):
        for k in range(max_sq):
            if ((i+k) < n) and ((j+k)<m) and (arr[i][j]== arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]):
                ans = max(ans, (k+1)**2)
                
print(ans)