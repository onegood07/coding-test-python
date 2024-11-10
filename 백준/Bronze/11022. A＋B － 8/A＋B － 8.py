T = int(input())
numbers = []

for _ in range(T):
    A, B = map(int, input().split())
    numbers.append(A)
    numbers.append(B)

numbers_A = numbers[0::2]
numbers_B = numbers[1::2]

for i in range(T):
    print(f"Case #{i + 1}: {numbers_A[i]} + {numbers_B[i]} = {numbers_A[i] + numbers_B[i]}")
