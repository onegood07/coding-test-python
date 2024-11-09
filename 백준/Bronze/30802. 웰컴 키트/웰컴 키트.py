N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

num_tshirt_bundles = 0
size_list = [S, M, L, XL, XXL, XXXL]

# 티셔츠 묶음 계산
for size_num in size_list:
    clothing_bundle = size_num // T

    if size_num == 0:
        num_tshirt_bundles += 0
    elif clothing_bundle > 0 and size_num % T == 0:
        num_tshirt_bundles += clothing_bundle
    elif clothing_bundle > 0 and size_num % T > 0:
        num_tshirt_bundles += (clothing_bundle + 1)
    else:
        num_tshirt_bundles += 1

# 펜 묶음 계산
buy_pen_bundles = N // P
buy_pen_unit = N % P

# 출력
print(num_tshirt_bundles)
print(f"{buy_pen_bundles} {buy_pen_unit}")
