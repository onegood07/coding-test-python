result = []

N = int(input())

for _ in range(N):
    A, B, C = map(int, input().split())
    if A == B and B == C:
        result.append(10000 + A * 1000)
    elif A == B:
        result.append(1000 + A * 100)
    elif B == C:
        result.append(1000 + B * 100)
    elif A == C:
        result.append(1000 + C * 100)
    else:
        result.append(max(A, B, C) * 100)

print(max(result))