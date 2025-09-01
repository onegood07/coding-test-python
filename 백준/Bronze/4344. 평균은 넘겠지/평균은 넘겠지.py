# 백준 - 4344

C = int(input())
results = []

for _ in range(C):
  scores = list(map(int, input().split()))
  count = 0

  avg = sum(scores[1:]) / scores[0]
  for idx in range(1, len(scores)):
    if scores[idx] > avg:
      count += 1

  results.append(count/scores[0])

for result in results:
  print(f"{result*100:.3f}%")
