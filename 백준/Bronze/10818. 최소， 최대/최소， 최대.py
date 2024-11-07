N = int(input())
numbers = list(map(int, input().split()))
max_num = -1_000_000
min_num = 1_000_000

for i in range(N):
    if numbers[i] >= max_num:
        max_num = numbers[i]
    if numbers[i] <= min_num:
        min_num = numbers[i]

print(f"{min_num} {max_num}")