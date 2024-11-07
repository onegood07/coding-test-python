N = int(input())

for i in range(N):
    split = ' ' * (N - (i + 1))
    star = "*" * (i + 1)
    print(f"{split}{star}")