a, b = input().split()

result = 0
if len(a) == len(b):
    for astr, bstr in zip(a, b):
        if astr != bstr:
            result+=1
    print(result)
elif len(a) < len(b):
    result_list = []
    for i in range(len(b)-len(a)+1):
        result = 0
        for astr, bstr in zip(a, b[i:i+len(a)]):
            if astr != bstr:
                result+=1
        result_list.append(result)
    print(min(result_list))

