def calculate_the_numbers(operation, num_a, num_b):
    return {"multiply": num_a * num_b,
     "divide": int(num_a / num_b),
     "add": num_a + num_b,
     "subtract": num_a - num_b
    }.get(operation, "Invalid operator")

input_operator = input()
number_a = int(input())
number_b = int(input())

result = calculate_the_numbers(input_operator, number_a, number_b)
print(result)