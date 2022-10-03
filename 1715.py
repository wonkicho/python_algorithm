import queue

card_queue = queue.PriorityQueue()

n = int(input())

for _ in range(n):
    card_num = int(input())
    card_queue.put(card_num)
    
print(card_queue.get())
    
s = 0

while card_queue.qsize() > 1:
    temp1 = card_queue.get()
    temp2 = card_queue.get()

    card_queue.put(temp1+temp2)
    s += (temp1+temp2)
    
print(s)
    