from collections import deque

#상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
k = int(input())

grid = [[0]*n for _ in range(n)]
for _ in range(k):
    x1, y1 = map(int, input().split())
    grid[x1-1][y1-1] = 1

L = int(input())
times = {}
for i in range(L):
    x, c = input().split()
    times[int(x)] = c

time = 1
direction = 1 #첫 방향은 오른쪽으로
x, y = 0, 0

#뱀꼬리 부분 기억하기 위함
snake_visit = deque()
snake_visit.append([x, y])


while True:
    x, y = x + dx[direction], y + dy[direction]
    if y < 0 or y > n-1 or x < 0 or x> n-1 or [x, y] in snake_visit:
        print(time)
        break
    else:
        #사과가 없다면
        if grid[x][y] != 1:
            tx, ty = snake_visit.popleft()
            grid[tx][ty] = 0
        
        #사과 있는 경우 + 1추가해서 2로 만듬
        #꼬리 기록하기
        grid[x][y] = 2
        snake_visit.append([x, y])

        #초, 방향 입력받은 것 확인
        if time in times.keys():
            c = times[time]

            #상우하좌
            # 시계방향쪽으로 회전
            if c == "L":
                direction = (direction-1) % 4
            else:
                # 시계반대방향으로 회전
                direction = (direction+1) % 4
        time += 1