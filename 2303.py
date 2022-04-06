from itertools import permutations

line = int(input())

max_list = []
num_list = [list(map(int, input().split())) for _ in range(line)]
for i in num_list:
    sum_list = [(sum(j) % 10, sum(j)) for j in list(permutations(i,3))]
    max_value = max(sum_list, key=lambda x : x[0])
    max_list.append(max_value)
    
mv = -999
rv = -999
idx = -999
result = 0
for id, i in enumerate(max_list):
    if mv < i[0]:
        mv = i[0]
        rv = i[1]
        idx = id
        result = idx+1
    elif mv == i[0]:
        result = id + 1
    

print(result)