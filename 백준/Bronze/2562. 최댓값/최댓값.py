max_number = 0
max_number_order = 0

for order in range(1, 10):
    N = int(input())
    if max_number <= N:
        max_number = N
        max_number_order = order

print(max_number)
print(max_number_order)