#구현, 시뮬레이션

chess_arr = [[0]*6 for _ in range(6)]
chess = [input() for _ in range(36)]


if len(set(chess)) == 36:
    for i in range(36):
        if i == 0:
            now = chess[i]
            prev = chess[i]

            x, y = ord(prev[0]) - 65, int(prev[1]) - 1
            chess_arr[x][y] = 1
            
        elif 0 < i < 35:
            now = chess[i]
            x1,y1 = ord(now[0]) - 65, int(now[1]) - 1
            x2,y2 = ord(prev[0]) - 65, int(prev[1]) - 1

            dist = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5

            if dist == (5 ** 0.5) and chess_arr[x1][y1] == 0:
                flag = 1
                chess_arr[x1][y1] = 1
                prev = now 
            else:
                flag = 0
                break

        else:
            now = chess[i]
            start_point = chess[0]

            x1,y1 = ord(now[0]) - 65, int(now[1]) - 1
            x2, y2 = ord(start_point[0]) - 65, int(start_point[1]) - 1

            dist = (((x1-x2) ** 2) + ((y1-y2) ** 2)) ** 0.5
            if dist == (5 ** 0.5):
                flag = 1
            else:
                flag = 0
else:
    flag = 0

if flag == 1:
    print("Valid")
else:
    print("Invalid")
