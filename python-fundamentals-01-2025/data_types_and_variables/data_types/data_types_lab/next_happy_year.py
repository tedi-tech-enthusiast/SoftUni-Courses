year = int(input())

while True:

    year += 1
    year_string = str(year)

    if len(set(year_string)) == len(year_string):
        break

print(year)