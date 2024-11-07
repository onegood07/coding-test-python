A = int(input())
B = int(input())
C = int(input())

number = str(A * B * C)
result = [0 for i in range(10)]

for i in range(len(number)): # 17037300
    result[int(number[i])] += 1

for i in range(len(result)):
    print(result[i])