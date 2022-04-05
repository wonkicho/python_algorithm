input_str = input()

answer = ""

#string split
for idx, s in enumerate(input_str.split('.')):
    
    #문자열 길이
    str_len = len(s)
    
    #길이가 짝수가 아닐 때 return 값 -1
    if str_len % 2 != 0:
        answer = '-1'
        break
    
    #짝수인 경우, 4로 떨어지지 않을 때, 4로 나눈 몫만큼 곱해서 문자열 더하기
    if str_len // 4 != 0:
        answer += "AAAA" * (str_len //4)
        #남은 문자열 길이 계산 : 14 / 4 : 몫 3 -> 14 - 12 = 2
        str_len -= (str_len // 4) * 4 
            
    if str_len // 2 != 0 : # 2로 나눈 몫이 0이 되지 않을 경우 -> 2 // 2 = 1
        answer += "BB" * (str_len// 2)
        str_len -= (str_len // 2) * 2
        
    #마지막 인덱스의 경우에 .을 안 붙이기 위함
    if idx != len(input_str.split('.')) -1 :    
        answer += '.'
    
print(answer)