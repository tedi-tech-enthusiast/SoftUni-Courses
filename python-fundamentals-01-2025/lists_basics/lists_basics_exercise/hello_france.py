ticket_cost = 150

price_limit_clothes = 50
price_limit_shoes = 35
price_limit_accessories = 20.5

bought_items = []
spend_amount = 0


items = input().split("|")

budget = float(input())

for item in items:
    currant_item = item.split("->")
    item_type = currant_item[0]
    item_price = float(currant_item[1])

    if (
        (item_type == "Clothes" and item_price <= price_limit_clothes) or
        (item_type == "Shoes" and item_price <= price_limit_shoes) or
        (item_type == "Accessories" and item_price <= price_limit_accessories)
    ):
        if budget >= item_price:
            budget -= item_price
            spend_amount += item_price
            item_price = item_price * 1.4
            bought_items.append(item_price)

print(*[f"{item:.2f}" for item in bought_items], sep=" ")

new_budget = sum(bought_items) + budget

profit = sum(bought_items) - spend_amount
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")