# [기억] try, except문 확인하기
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break