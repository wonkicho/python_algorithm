
n = int(input())

word_list = []

for _ in range(n):
    word = input()
    word_list.append(word)

dict = {}
for word in word_list:
    sqrt = len(word) - 1

    for c in word:
        if c in dict:
            dict[c] += pow(10 ,sqrt)
        else:
            dict[c] = pow(10, sqrt)

        sqrt -= 1

dict = sorted(dict.values(), reverse=True)

result,m = 0,9


for value in dict:
  result += value * m
  m -= 1

print(result)
