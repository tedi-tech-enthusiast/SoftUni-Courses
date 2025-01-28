n = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(n):
    currant_number = int(input())

    if currant_number >= 0:
        positive_numbers.append(currant_number)
    else:
        negative_numbers.append(currant_number)

print(positive_numbers)
print(negative_numbers)

print(f'Count of positives: {len(positive_numbers)}')
print(f'Sum of negatives: {sum(negative_numbers)}')

