n = int(input())
v = int(input())
vote_list = list(map(int, input().split()))

stu = [0] * 101
temp = [] #사진틀

for c in vote_list:

    #이미 꽉 차 있는 경우
    if len(temp) == n:
        if c in temp:
            stu[c] += 1
        else:
            mid = temp[0] 
            mc = stu[mid] #학생 번호, 투표 받은 수
            
            for i in temp[1:]:
                if mc > stu[i]:
                    mc = stu[i]
                    mid = i
                
            temp.remove(mid)
            stu[mid] = 0 

            temp.append(c)
            stu[c] += 1
        
    #사진틀 꽉 차있지 않은 경우
    else:
        if c in temp:
            stu[c] += 1
        else:
            temp.append(c)
            stu[c] += 1
        
result = [[i,stu[i]] for i in temp]
result.sort(key = lambda x : x[0])
result = [r[0] for r in result]

print(*result)


