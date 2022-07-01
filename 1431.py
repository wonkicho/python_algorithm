n = int(input())

def sum_dial(serial):
    res = 0
    for i in serial:
        if i.isdigit():
            res += int(i)
    return res
print(sum_dial("Z20"))

arr = []
for i in range(n):
    a = input()
    arr.append(a)
    
arr.sort(key = lambda x : (len(x), sum_dial(x), x))

for i in arr:
    print(i)