number_of_lines = int(input())

tank_capacity = 255


for line in range(number_of_lines):
    liters_of_water = int(input())

    # not enough capacity for the volume of water
    if tank_capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue

    tank_capacity -= liters_of_water

print(255 - tank_capacity)