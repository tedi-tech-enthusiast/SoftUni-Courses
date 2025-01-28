list_with_numbers = input().split()
opposite_numbers = []

for currant_number in list_with_numbers:
    opposite_number = -int(currant_number)
    opposite_numbers.append(opposite_number)

print(opposite_numbers)