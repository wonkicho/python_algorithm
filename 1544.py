from collections import deque


n = int(input())
word_list = []
for _ in range(n):
    word = input()
    word_list.append(word)
    
for i in range(n):
    dq = deque(word_list[i])
    
    while True:
        dq.append(dq.popleft())
        print(dq)
        temp = "".join(dq)
        if temp == word_list[i]:
            break
        
        if temp in word_list:
            idx = word_list.index(temp)
            word_list.pop(idx)
            word_list.insert(idx, word_list[i])
            

print(len(set(word_list)))