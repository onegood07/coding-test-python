T = int(input())
result = []

def assign_room_number(H, W, N):
    if N % H == 0:
        num = (N // H)
        floor = H
    else:
        num = (N // H) + 1
        floor = N % H

    result.append(f"{floor}{num:02d}")

for _ in range(T):
    H, W, N = map(int, input().split())
    assign_room_number(H, W, N)

for i in range(T):
    print(result[i])