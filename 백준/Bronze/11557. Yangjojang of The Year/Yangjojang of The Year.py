result = []
T = int(input())

for _ in range(T):
    calculate_alcohol = []
    N = int(input())

    for _ in range(N):
        U, A = input().split()
        calculate_alcohol.append(U)
        calculate_alcohol.append(int(A))
    
    alcohol_intakes = list(zip(calculate_alcohol[::2], calculate_alcohol[1::2]))
    calculate_alcohol_intakes = max(alcohol_intakes, key= lambda x: x[1])
    result.append(calculate_alcohol_intakes[0])
        
for i in result:
    print(i)