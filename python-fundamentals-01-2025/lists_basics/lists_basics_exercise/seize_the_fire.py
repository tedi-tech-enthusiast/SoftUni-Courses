from turtledemo.penrose import start

fires = input().split("#")

amount_of_water = int(input())

effort = 0
list_of_cells = []

for fire in fires:
    currant_fire = fire.split(" = ")
    fire_type = currant_fire[0]
    fire_range = int(currant_fire[1])

    if amount_of_water >= fire_range:

        if (
                (fire_type == "High" and 81 <= fire_range <= 125)
                or (fire_type == "Medium" and 51 <= fire_range <= 80)
                or (fire_type == "Low" and 1 <= fire_range <= 50)
        ):

            amount_of_water -= fire_range
            effort += fire_range * 0.25
            list_of_cells.append(fire_range)

print("Cells:")

for cell in list_of_cells:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(list_of_cells)}")