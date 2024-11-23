word = input()
result = []

for one in word:
    if 'A' <= one and one <= 'Z':
        result.append(chr(ord(one) + 32))
    else:
        result.append(chr(ord(one) - 32))

print(''.join(result))