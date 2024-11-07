count = int(input())
numbers = list(input())
sum = 0

for i in range(count):
    sum += int(numbers[i])

print(f"{sum}")
