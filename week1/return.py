# return what is?

def add(a, b):
    sum = a + b
    return sum
    print("This line will never be executed because it is after the return statement.")

result = add(1, 2)

print("The result of the addition is:", result)