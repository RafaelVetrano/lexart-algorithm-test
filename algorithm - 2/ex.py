def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

functions_map = {
    "addition": addition,
    "subtraction": subtraction,
    "multiplication": multiplication,
    "division": division
}

a = 5
b = 2

result_addition = functions_map["addition"](a, b)
print("Addition result:", result_addition)

result_subtraction = functions_map["subtraction"](a, b)
print("Subtraction result:", result_subtraction)

result_multiplication = functions_map["multiplication"](a, b)
print("Multiplication result:", result_multiplication)

result_division = functions_map["division"](a, b)
print("Division result:", result_division)