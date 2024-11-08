H, M = map(int, input().split())
result_H = 0

minutes = (H * 60 + M) - 45

if (minutes // 60) == -1:
    result_H = 23
else:
    result_H = (minutes // 60)

print(f"{result_H} {minutes % 60}")