n = int(input())

#dp 저장 테이블
d = [0] * (n+1)

for i in range(2, n+1):
    
    #현재의 수에서 1 빼는 경우, 1 더하는 것은 횟 수 
    d[i] = d[i-1] + 1
    
    #2로 나뉘어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
        
    #3으로 나뉘어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
        
print(d[n])
