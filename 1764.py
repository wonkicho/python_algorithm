n, m = map(int, input().split())

name_dict = {}
for i in range(1, n+m+1):
    name = input()

    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] += 1

result = [k for k, v in name_dict.items() if v > 1]
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])
