n, qn = map(int, input().split())
num_arr = list(map(int, input().split()))

prefix_sum = [0]
temp = 0
for i in num_arr:
    temp += i
    prefix_sum.append(temp)
    
 
for i in range(qn):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])