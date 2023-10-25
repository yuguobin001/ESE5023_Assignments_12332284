from itertools import product

def Find_expression():
    digits = "123456789"
    operators = ["", "+", "-"]
    operator_comb = product(operators, repeat=8)
    Total_solutions = [0] * 100
    for ops in operator_comb:
        expression = ""
        for i in range(8):
            expression += digits[i] + ops[i]
        expression += digits[-1]
        result = eval(expression)

        if 1 <= result <= 100:
            Total_solutions[result - 1] = Total_solutions[result - 1]+ 1
    return Total_solutions

Total_solutions = Find_expression()
max_solutions = max(Total_solutions)
min_solutions = min(Total_solutions)
max_indices = [i + 1 for i, count in enumerate(Total_solutions) if count == max_solutions]
min_indices = [i + 1 for i, count in enumerate(Total_solutions) if count == min_solutions]
print(f"maximum ({max_solutions}): {max_indices}")
print(f"minimum ({min_solutions}): {min_indices}")
