result = []
N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())
    if r == (e - c):
        result.append('does not matter')
    elif r > (e - c):
        result.append('do not advertise')
    else:
        result.append('advertise')

for one in result:
    print(one)