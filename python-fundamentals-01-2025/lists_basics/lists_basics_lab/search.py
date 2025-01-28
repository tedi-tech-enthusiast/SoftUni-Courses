n = int(input())
special_word = input()

full_list = []
special_word_list = []

for _ in range(n):
    currant_string = input()
    full_list.append(currant_string)

    if special_word in currant_string:
        special_word_list.append(currant_string)

print(full_list)
print(special_word_list)