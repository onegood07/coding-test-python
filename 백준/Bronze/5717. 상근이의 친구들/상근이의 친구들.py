result = []

while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    result.append(M + F)

for one in result:
    print(one)