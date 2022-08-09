n = int(input())

tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)

result = 0
for idx, t in enumerate(tip):
    ri = idx + 1

    real_tip = t - (ri - 1)

    if real_tip > 0:
        result += real_tip
    else:
        result += 0

print(result)
