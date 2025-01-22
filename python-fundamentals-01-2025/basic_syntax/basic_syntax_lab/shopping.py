budget = int(input())
spending_counter = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break
    item_price = int(command)

    if spending_counter + item_price > budget:
        print("You went in overdraft!")
        break

    spending_counter += item_price
