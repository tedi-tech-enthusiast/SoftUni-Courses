money_as_string = input().split(", ")
number_of_beggars = int(input())

money_as_integers = []

# list comprehension
# money_as_integers = [int(money) for money in money_as_string]

for money in money_as_string:
    money_as_integers.append(int(money))

beggars_sums = []
start_index = 0

for currant_beggar in range(number_of_beggars):
    currant_beggar_sum = 0

    for currant_index in range(start_index, len(money_as_integers), number_of_beggars):
        currant_beggar_sum += money_as_integers[currant_index]

    beggars_sums.append(currant_beggar_sum)
    start_index += 1

print(beggars_sums)