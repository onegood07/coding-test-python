S = input()

alpha_indices = [i for i in range(97, 123)]
alpha_orders = [-1 for _ in range(len(alpha_indices))]

for word_index, word in enumerate(S):
    for alpha_index, alpha_index_value in enumerate(alpha_indices):
        if ord(word) == alpha_index_value and alpha_orders[alpha_index] == -1:
            alpha_orders[alpha_index] = word_index

result = " ".join(map(str, alpha_orders))
print(result)