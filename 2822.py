score_list = []

for i in range(8):
    score = int(input())
    score_list.append((i,score))
    
score_sort_list = sorted(score_list, reverse=True, key=lambda x : x[1])

sum_value = 0
idx_list = []
for i in score_sort_list[:5]:
    sum_value += i[1]
    idx_list.append(i[0])
    
idx_list = sorted(idx_list)

print(sum_value)
for i in idx_list:
    print(i + 1, end=' ')