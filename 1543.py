input_str = input()
find_str = input()

fs_len = len(find_str)

i = 0
cnt = 0
while i <= len(input_str) - len(find_str):
    if input_str[i : i + fs_len] == find_str:
        cnt += 1
        i += fs_len 
    else:
        i += 1

print(cnt)