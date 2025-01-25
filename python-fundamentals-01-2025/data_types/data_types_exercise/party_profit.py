companions_count = int(input())
number_of_days = int(input())

coins = 0

for currant_day in range(1, number_of_days + 1):

    if currant_day % 10 == 0:
        companions_count -= 2

    if currant_day % 15 == 0:
        companions_count += 5

    if currant_day % 3 == 0:
        coins -= 3 * companions_count

    if currant_day % 5 == 0:
        coins += 20 * companions_count
        if currant_day % 3 == 0:
            coins -= 2 * companions_count

    coins += 50
    coins -= 2 * companions_count

coins_per_companion = int(coins // companions_count)
print(f'{companions_count} companions received {coins_per_companion} coins each.')


