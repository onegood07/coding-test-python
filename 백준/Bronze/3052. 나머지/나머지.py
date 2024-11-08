modulus_values = []

for _ in range(10):
    num = int(input())
    modulus_values.append(num % 42)

print(len(set(modulus_values)))

