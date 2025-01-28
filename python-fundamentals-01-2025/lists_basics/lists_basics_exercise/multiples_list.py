factor = int(input())
count = int(input())

numbers = []
next_num = 0

for multiplier in range(1, count + 1):
    numbers.append(multiplier * factor)

print(numbers)