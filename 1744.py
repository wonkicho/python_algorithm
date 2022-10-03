import queue

plus_queue = queue.PriorityQueue()
minus_queue = queue.PriorityQueue()

zero, one = 0, 0
s = 0
n = int(input())
for _ in range(n):
    data = int(input())
    
    if data > 1 :
        plus_queue.put(data*-1)
    elif data < 0:
        minus_queue.put(data)
        
    elif data == 0:
        zero += 1
    elif data == 1:
        one += 1
        

while plus_queue.qsize() > 1:
    n1 = plus_queue.get() * -1
    n2 = plus_queue.get() * -1
    s += (n1 * n2)

if plus_queue.qsize() > 0:
    s += plus_queue.get() * -1    

while minus_queue.qsize() > 1:
    n1 = minus_queue.get() 
    n2 = minus_queue.get() 
    s += (n1 * n2)
    
if minus_queue.qsize() >0:
    if zero == 0:
        s += minus_queue.get()
        
s += one
print(s)