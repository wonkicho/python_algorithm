n = int(input())
num_list = list(map(int, input().split()))

s = 0.0

for i in num_list:
    s += i
    
print(s*100 /max(num_list) / n)
