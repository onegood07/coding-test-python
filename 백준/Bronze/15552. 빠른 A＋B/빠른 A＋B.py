import sys
T = int(input())

for _ in range(0, T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)