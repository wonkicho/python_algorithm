N = int(input())
M = int(input())

brd = [[0 for _ in range(N)] for _ in range(N)]

#아래, 오른, 위, 아래
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


x,y=0,0
num = N**2
i = 0
ax, ay = 0, 0

while True:
    brd[x][y] = num
    
    nx = x + dir_x[i]
    ny = y + dir_y[i]
    if nx >= N or ny>=N or nx <= -1 or ny<=-1 or brd[nx][ny] != 0:
        i += 1
        if i == 4:
            i = 0
        continue
    
    # if num == M:
    #     ax, ay = x+1, y+1
        
    x, y = nx, ny
    num -= 1
    
    if num == 1 :
        break
brd[x][y] = num

for i in range(N):
    for j in range(N):
        if brd[i][j] == M:
            ax, ay = i + 1, j + 1
            
    print(*brd[i])
print(ax, ay)