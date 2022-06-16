#정답
d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

M, N = map(int, input().split())
li = []

for i in range(M, N+1):
    s = ' '.join([d[c] for c in str(i)])
    li.append([i, s])
    
li.sort(key=lambda x:x[1])
for i in range(len(li)):
    if i%10 == 0 and i!= 0:
        print()
    print(li[i][0], end=' ')



#틀린 답
"""
M, N  = map(int, input().split(' '))

number_dict = {"0" : "zero", "1" : "one", "2" : "two", "3":"three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight" , "9" : "nine"}

#일의 자리
digit_one = []
#십의 자리
digit_two = []

n = [str(i) for i in range(M, N+1)]
for num in n:
    if len(num) == 1:
        digit_one.append(number_dict[num])
    else:
        temp = [number_dict[n] for n in list(num)]
        digit_two.append(temp)
        
rv_number_dict = {v : k for k, v in number_dict.items()}
result = [rv_number_dict[i] for i in sorted(digit_one)]

digit_two = sorted(digit_two)
for num_list in digit_two:
    num = rv_number_dict[num_list[0]] + rv_number_dict[num_list[1]]
    result.append(num)

for i in range(len(result)):
    if i%10 == 0 and i!= 0:
        print()
    print(result[i], end=' ')
"""