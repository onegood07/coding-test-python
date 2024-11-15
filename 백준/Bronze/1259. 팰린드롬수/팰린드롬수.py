result = []
result_index = 0

while True:
    num = int(input())
    if num == 0:
        break
    num = str(num)
    result.append('yes')
    
    for index in range(len(num)):
        if num[index] != num[len(num) - (index + 1)]:
            result[result_index] = 'no'
            break
    
    result_index += 1
     
for one_result in result:
    print(one_result)