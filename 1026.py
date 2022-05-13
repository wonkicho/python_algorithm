N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=False)
B = sorted(B, reverse=True)

s = 0
for av, bv in zip(A,B):
    s += av*bv
    
print(s)