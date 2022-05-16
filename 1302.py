N = int(input())

book_list = [input() for _ in range(N)]
book_dict = {}

for i in book_list:
    if i not in book_dict.keys():
        book_dict[i] = 1
    else:
        book_dict[i] += 1
        
mv = -9999
mb = ""
for k, v in book_dict.items():
    if v > mv:
        mv = v
        mb = k
    elif mv == v:
        if (mb < k) == False:
            mb = k
        else:
            pass
        
print(mb)