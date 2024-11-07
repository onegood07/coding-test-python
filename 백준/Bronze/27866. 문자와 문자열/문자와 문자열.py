S = input()
i = int(input())

for index, j in enumerate(S):
    if index + 1 == i:
        print(f"{j}")