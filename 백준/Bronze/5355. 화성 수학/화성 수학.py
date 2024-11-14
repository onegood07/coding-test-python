T = int(input())
result = []

for _ in range(T):
    N = input().split()
    result_one = float(N[0])

    for n in range(1, len(N)):
        if N[n] == '@':
            result_one *= 3
        elif N[n] == '%':
            result_one += 5
        elif N[n] == '#':
            result_one -= 7
    
    result.append(result_one)

for i in result:
    print(f"{i:.2f}")