gifts_list = input().split()

final_gift_list = []


while True:
    command = input()
    if command == "No Money":
        break

    parts = command.split()
    action = parts[0]
    gift = parts[1]

    if action == "OutOfStock":

        # заменям стойностите на всички съвпадения с "gift" на "None"
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = "None"

    elif action == "Required":
        index = int(parts[2])

        # случай, че индексът е коректен заменям подаръка на конкретната позиция с "gift"
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift

    elif action == "JustInCase":
        # заменям последния подарък с "gift"
        gifts_list[-1] = gift

for currant_gift in gifts_list:
    if currant_gift != "None":
        final_gift_list.append(currant_gift)

print(" ".join(final_gift_list))