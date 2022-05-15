import sys

sys.stdin = open('input.txt', 'r')

#모음 반드시 하나 이상
#모음 및 자음 3개 연속 x
#같은 글자 연속 x , ee oo 가능


# 모음 확인
def check_vowel(string):
    for c in string:
        if c in 'aeiou':
            return True
    return False

#자음 3, 모음 3 연속
def check_3vowel_3con(string):
    if len(string) < 3:
        return True
    elif len(string) == 3:
        check = ''
        for i in range(3):
            if string[i] in 'aeiou':
                check += 'v'
            else:
                check += 'c'
        if check == 'vvv' or check == 'ccc':
            return False
        else:
            return True
        
    for i in range(len(string) - 2):
        check = ''
        for j in range(3):
            if string[i+j] in 'aeiou':
                check += 'v'
            else:
                check += 'c'
        if check == 'vvv' or check == 'ccc':
            return False
    return True
        
def check_same_chr(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            if string[i] == 'e' or string[i] == 'o':
                return True
            else:
                return False
            
        

while True:
    s = input()
    if s == 'end':
        break
    
    if check_vowel(s) and check_3vowel_3con(s) and check_same_chr(s):
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
        