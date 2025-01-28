n = int(input())

list_of_numbers = []
filtered_numbers = []

for _ in range(n):
    currant_number = int(input())
    list_of_numbers.append(currant_number)

command = input()

if command == 'even':
    for number in list_of_numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == 'odd':
    for number in list_of_numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == 'negative':
    for number in list_of_numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == 'positive':
    for number in list_of_numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)