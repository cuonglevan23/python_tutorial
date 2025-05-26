# exam calculator

num_1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num_2 = float(input("Enter the second number: "))

if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
elif operator == '/':
    if num_2 != 0:
        result = num_1 / num_2
    else:
        result = "Error: Division by zero is not allowed."


print("The result is:", result)