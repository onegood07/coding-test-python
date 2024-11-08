ascending = [i for i in range(1, 9)]
descending = [j for j in range(8, 0, -1)]

numbers = list(map(int, input().split()))

if numbers == ascending:
    print("ascending")
elif numbers == descending:
    print("descending")
else:
    print("mixed")