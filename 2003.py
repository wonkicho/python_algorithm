n, m = map(int, input().split())

result = 0
s_list = list(map(int, input().split()))

for i in range(len(s_list)):
    temp_sum = 0
    for j in range(i, len(s_list)):
        temp_sum += s_list[j]
        if temp_sum == m:
            result += 1
            break
        elif temp_sum > m:
            break
        
print(result)