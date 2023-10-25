from itertools import product
def Find_expression(x):
    digits = "123456789"
    operators = ["", "+", "-"]
    operator_comb = product(operators, repeat=8)
    for ops in operator_comb:
        expression = ""
        for i in range(8):
            expression += digits[i] + ops[i]
        expression = expression + digits[-1]
        result = eval(expression)
        if result == x:
            print(expression + " = " + str(x))
Find_expression(50)