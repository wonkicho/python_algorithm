input_str = input()

answer = ""
for idx, s in enumerate(input_str.split('.')):
    str_len = len(s)
    if str_len % 2 != 0:
        answer = '-1'
        break
    
    if str_len // 4 != 0:
        answer += "AAAA" * (str_len //4)
        str_len -= (str_len // 4) * 4
            
    if str_len // 2 != 0 :
        answer += "BB" * (str_len// 2)
        str_len -= (str_len // 2) * 2
        
    if idx != len(input_str.split('.')) -1 :    
        answer += '.'
    
print(answer)