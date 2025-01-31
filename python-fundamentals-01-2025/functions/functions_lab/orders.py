def calculate_total_price(item, quantity):
    return {"coffee": 1.50 * quantity,
     "water": 1.00 * quantity,
     "coke": 1.40 * quantity,
     "snacks": 2.00 * quantity
    }.get(item, "Invalid operator")

input_item = input()
input_quantity = int(input())

result = calculate_total_price(input_item, input_quantity)
print(f"{result:.2f}")