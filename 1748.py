

N = int(input())
ans = 0

for i in range(1, len(str(N))):
    ans += int('9' + (i-1)*'0')*i
    

ans += (int(N) - 10 ** (len(str(N)) - 1) + 1) * len(str(N))

print(ans)