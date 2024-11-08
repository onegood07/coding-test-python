def is_right_triangle(A, B, C):
    hypotenuse = max(A, B, C)
    others = [A, B, C]
    others.remove(hypotenuse)

    if (hypotenuse ** 2 == others[0] ** 2 + others[1] ** 2):
        return "right"
    else:
        return "wrong"

results = []

while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break

    results.append(is_right_triangle(A, B, C))

for result in results:
    print(result)