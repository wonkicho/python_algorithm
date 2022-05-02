"""
1,2,2,3,3,3,4,4,4,4,5,5,5,5,5....
"""

a, b = map(int, input().split(' '))


number_list = []
num = 1
for i in range(b+1):
    for _ in range(i):
        if len(number_list) == b:
            break
        number_list.append(i)

print(sum(number_list[a-1:]))
