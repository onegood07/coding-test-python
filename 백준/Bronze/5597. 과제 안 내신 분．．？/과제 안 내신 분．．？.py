N = [i for i in range(1, 31)]

for _ in range(28):
    n = int(input())
    N.remove(n)

print(min(N))
print(max(N))