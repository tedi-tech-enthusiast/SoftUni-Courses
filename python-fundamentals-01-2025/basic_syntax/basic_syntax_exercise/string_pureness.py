number_of_strings = int(input())

for currant_strings in range(number_of_strings):
    currant_string = input()

    if "," in currant_string or "." in currant_string or "_" in currant_string:
        print(f"{currant_string} is not pure!")
    else:
        print(f"{currant_string} is pure.")