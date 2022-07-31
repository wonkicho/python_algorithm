import sys

n = int(input())

for _ in range(n):
    p = int(input())
    cnt = 1
    temp = []
    for _ in range(p):
        a, b = map(int,sys.stdin.readline().split())
        temp.append([a, b])

    temp.sort()
    Max_score = temp[0][1]

    for i in range(p):
        if Max_score > temp[i][1]:
            cnt += 1
            Max_score = temp[i][1]
            
            
    print(cnt)
