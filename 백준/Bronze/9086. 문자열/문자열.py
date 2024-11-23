T = int(input())
result = []

for _ in range(T):
    word = input()
    result.append(word[0] + word[-1])

for one in result:
    print(one)