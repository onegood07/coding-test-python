N = int(input())
score = list(map(int, input().split()))
avg_score = 0

for one_score in score:
    M = max(score)
    avg_score += one_score / M * 100

print(avg_score/N)