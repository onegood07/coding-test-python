result = []
T = int(input())

for _ in range(T):
    R, S = input().split()
    result_word = ""
    for i in range(len(S)):
        result_word += f"{S[i] * int(R)}"

    result.append(result_word)

for i in range(len(result)):
    print(result[i])
