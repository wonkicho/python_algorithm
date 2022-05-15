A, P = map(int, input().split())

num_list = [A]
while True:
    v = 0
    for s in str(num_list[-1]):
        v += int(s) ** P

    if v in num_list:
        break

    num_list.append(v)

print(num_list.index(v))