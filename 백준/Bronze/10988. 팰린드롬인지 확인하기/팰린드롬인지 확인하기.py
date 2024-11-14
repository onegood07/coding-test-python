word = input()
result = 0

for i in range(len(word)):
    if word[i] != word[len(word) - (i + 1)]:
        result = 0
        break
    else:
        result = 1

print(result)