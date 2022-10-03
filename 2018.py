n = int(input())

cnt = 1

s, e = 1, 1
total = 1

while e != n:
    if total == n:
        cnt += 1
        e += 1
        total += e
    elif total > n:
        total -= s
        s += 1    
    else:
        e += 1
        total += e
        
print(cnt)