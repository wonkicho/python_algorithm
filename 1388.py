r, c = map(int, input().split())
arr = []
for i in range(r):
    s = input()
    arr.append(list(s))
    
result = 0
for i in range(r):
    temp_r = ''
    for j in range(c):
        if arr[i][j] == '-':    
            if arr[i][j] != temp_r:
                result += 1
        temp_r = arr[i][j]

for j in range(c):
    temp_c = ''
    for i in range(r):
        if arr[i][j] == "|":
                if arr[i][j] != temp_c:
                    result += 1
        temp_c = arr[i][j]

                
print(result)

        
