number_of_massages = int(input())

for currant_message in range(number_of_massages):
    currant_number = int(input())
    message = ""

    if currant_number == 88:
        message = "Hello"
    elif currant_number == 86:
        message = "How are you?"
    elif currant_number < 88:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)
