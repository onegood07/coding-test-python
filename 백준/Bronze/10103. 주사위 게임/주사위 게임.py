score = [100, 100]
n = int(input())

for _ in range(n):
    A, B = map(int, input().split())
    if A == B:
        continue
    elif A > B:
        score[1] -= A
    else:
        score[0] -= B

print(score[0])
print(score[1])