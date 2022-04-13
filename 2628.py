x, y = map(int, input().split())
n = int(input())

x_list = [0, x]
y_list = [0, y]
for i in range(n):
    k, l = map(int, input().split())
    
    if k == 0:
        y_list.append(l)
        
    else:
        x_list.append(l)
        
x_list.sort()
y_list.sort()

max_v = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        w = x_list[i] - x_list[i-1]
        h = y_list[j] - y_list[j-1]
        max_v = max(max_v, w*h)
        
print(max_v)
