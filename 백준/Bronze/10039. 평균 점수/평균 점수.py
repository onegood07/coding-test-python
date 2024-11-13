avg_score = 0

for _ in range(5):
    score = int(input())
    if score < 40:
        avg_score += 40
        continue
    avg_score += score

print(int(avg_score/5))