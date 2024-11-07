T = int(input())
plus = []
for i in range(T):
    A, B = map(int, input().split())
    plus.append(A + B)

for one in plus:
    print(one)
