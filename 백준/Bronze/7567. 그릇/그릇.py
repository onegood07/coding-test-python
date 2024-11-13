bowls = input()
bowls_len = 10

for i in range(1, len(bowls)):
    if bowls[i] == bowls[i-1]:
        bowls_len += 5
    else:
        bowls_len += 10

print(bowls_len)