N = int(input())

card = [i for i in range(1, N+1)]
result = []
while len(card) != 1:
    discard = card.pop(0)
    tmp = card.pop(0)
    card.append(tmp)
    result.append(discard)
    
for i in result:
    print(i, end = ' ')
print(card[0])