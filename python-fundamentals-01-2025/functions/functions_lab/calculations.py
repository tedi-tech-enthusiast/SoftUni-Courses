def calculate_the_numbers(operation, num_a, num_b):
    if operation == "multiply":
        return num_a * num_b

    elif operation == "divide":
        return int(num_a / num_b)

    elif operation == "add":
        return num_a + num_b

    elif operation == "subtract":
        return num_a - num_b


input_operator = input()
number_a = int(input())
number_b = int(input())

result = calculate_the_numbers(input_operator, number_a, number_b)
print(result)
