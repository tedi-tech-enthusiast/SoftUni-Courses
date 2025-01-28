numbers_string_list = input().split()
numbers_integer_list = []

n = int(input())

for currant_number in numbers_string_list:
    number = int(currant_number)
    numbers_integer_list.append(number)


for _ in range(n):  # Премахва най-малкото число 'n' пъти
    numbers_integer_list.remove(min(numbers_integer_list))

print(*numbers_integer_list, sep=", ")