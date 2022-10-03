n, m = map(int, input().split())

coin_list = []
for _ in range(n):
    coin_list.append(int(input()))
    
result = 0
for i in range(n-1, -1, -1):
    if coin_list[i] <= m:
        c = m // coin_list[i]
        m -= c * coin_list[i]
        result += c
        
print(result)