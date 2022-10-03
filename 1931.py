n = int(input())

t = []
for _ in range(n):
    s, e = map(int, input().split())
    t.append([e, s])
    
t.sort()


mt_end = -1
cnt = 0
for i in range(n):
    if t[i][1] >= mt_end:
        mt_end = t[i][0]
        cnt += 1
        
    
    
print(cnt)