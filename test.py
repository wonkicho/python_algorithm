office = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]]
k = 2


for i in range(len(office)-k+1):
    print(office[i:][:i+k])
    