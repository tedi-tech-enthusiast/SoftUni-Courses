currant_string = input()

while currant_string != "End":

    if currant_string != "SoftUni":
        new_string = ""

        for character in currant_string:
            new_string += character * 2

        print(new_string)

    currant_string = input()