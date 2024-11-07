def calculate_quiz_score(quiz_answer):
    score_result = [0 for i in range(len(quiz_answer))]
    score = 0
    sum = 0

    for index in range(len(quiz_answer)):
        if quiz_answer[index] == 'O':
            score += 1
            score_result[index] = score
        else:
            score = 0
    
    for i in score_result:
        sum += int(i)
    
    return sum

result = []
T = int(input())

for _ in range(T):
    answer = input()
    result.append(calculate_quiz_score(answer))

for i in range(T):
    print(result[i])
