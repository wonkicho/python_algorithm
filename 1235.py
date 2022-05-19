N = int(input())

students = []
for _ in range(N):
    s = input()
    students.append(s)

temp = []
str_len = len(students[0])
start_idx = 1
while True:

    temp = []
    for i in range(len(students)):
        num = students[i][str_len::-1][:start_idx]
        temp.append(num)
    
    if len(set(temp)) < N:
        start_idx += 1
    else:
        print(start_idx)
        break

