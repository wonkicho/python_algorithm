n = int(input())
h = list(map(int, input().split()))
ans = [0] * n

# 2, 1, 1, 0
#[0,0,0,0]
# 1, 2, 3,4
for i in range(1, n+1):
    t = h[i-1]
    cnt = 0
    for j in range(n):
        
        if ans[j] == 0 and cnt == t: 
            ans[j] = t
            break
        elif ans[j] == 0:
            cnt += 1
            
print(*ans)