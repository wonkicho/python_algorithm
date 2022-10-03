n = int(input())
board = [[chr(46)] * n for _ in range(n)]

direction_list = input()

s1, s2 = 0, 0

#위 아래 왼 오
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for d in direction_list:
    if d == "U":
        if s1 + dx[0] < 0 or s1 + dx[0] > n-1 or s2 + dy[0] < 0 or s2 + dy[0] > n-1:
            continue
        
        elif board[s1][s2] == chr(46) or board[s1][s2] == chr(124):
            board[s1][s2] = chr(124)
            s1 = s1 + dx[0]
            s2 = s2 + dy[0]
            board[s1][s2] = chr(124)
        elif board[s1][s2] == chr(45):
            board[s1][s2] = chr(43)
            s1 = s1 + dx[0]
            s2 = s2 + dy[0]
            board[s1][s2] = chr(124)
        else:
            s1 = s1 + dx[0]
            s2 = s2 + dy[0] 
            board[s1][s2] = chr(124)
    elif d == "D" :
        if s1 + dx[1] < 0 or s1 + dx[1] > n-1 or s2 + dy[1] < 0 or s2 + dy[1] > n-1:
            continue
        elif board[s1][s2] == chr(46) or board[s1][s2] == chr(124):
            board[s1][s2] = chr(124)
            s1 = s1 + dx[1]
            s2 = s2 + dy[1]
            board[s1][s2] = chr(124)
        
        elif board[s1][s2] == chr(45):
            board[s1][s2] = chr(43)
            s1 = s1 + dx[1]
            s2 = s2 + dy[1]
            board[s1][s2] = chr(124)
            
        else:
            s1 = s1 + dx[1]
            s2 = s2 + dy[1]
            board[s1][s2] = chr(124)
        
    
    elif d == "L":
        if s1 + dx[2] < 0 or s1 + dx[2] > n-1 or s2 + dy[2] < 0 or s2 + dy[2] > n-1:
            continue
        elif board[s1][s2] == chr(46) or board[s1][s2] == chr(45):
            board[s1][s2] = chr(45)
            s1 = s1 + dx[2]
            s2 = s2 + dy[2]
            board[s1][s2] = chr(45)
        elif board[s1][s2] == chr(124):
            board[s1][s2] = chr(43)
            s1 = s1 + dx[2]
            s2 = s2 + dy[2]
            board[s1][s2] = chr(45)
        else:
            s1 = s1 + dx[2]
            s2 = s2 + dy[2] 
            board[s1][s2] = chr(45)
        
        
    elif d == "R":
        if s1 + dx[3] < 0 or s1 + dx[3] > n-1 or s2 + dy[3] < 0 or s2 + dy[3] > n-1:
            continue
        elif board[s1][s2] == chr(46) or board[s1][s2] == chr(45):
            board[s1][s2] = chr(45)
            s1 = s1 + dx[3]
            s2 = s2 + dy[3]
            board[s1][s2] = chr(45)
        elif board[s1][s2] == chr(124):
            board[s1][s2] = chr(43)
            s1 = s1 + dx[3]
            s2 = s2 + dy[3]
            board[s1][s2] = chr(45)
        else:
            s1 = s1 + dx[3]
            s2 = s2 + dy[3] 
            board[s1][s2] = chr(45)
    

for i in range(n):
    print(''.join(board[i]))