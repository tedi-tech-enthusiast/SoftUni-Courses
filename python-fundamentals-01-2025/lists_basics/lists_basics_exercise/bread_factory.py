events = input().split("|")

total_energy = 100
total_coins = 100

bakery_is_open = True


for event in  events:
    event_item = event.split("-")
    event_type = event_item[0]
    event_value = int(event_item[1])

    if event_type == "rest":
        initial_energy = total_energy
        total_energy += event_value

        if total_energy > 100:
            total_energy = 100

        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_type == "order":
        if total_energy >= 30:
            total_coins += event_value
            total_energy -= 30
            print(f"You earned {event_value} coins.")

        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            bakery_is_open = False
            break

if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {event_type}.")