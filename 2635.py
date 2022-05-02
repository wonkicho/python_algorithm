n = int(input())

idx = 0
len_result = 0

for i in range(n+1):
    result_list = [n, i]
    idx = 0
    while True:
        temp = result_list[idx] - result_list[idx + 1]
        idx += 1
        if temp < 0:
            break
        
        result_list.append(temp)
        if len_result < len(result_list):
            len_result = len(result_list)
            result = result_list[:]


print(len_result)
print(' '.join(map(str,result)))
