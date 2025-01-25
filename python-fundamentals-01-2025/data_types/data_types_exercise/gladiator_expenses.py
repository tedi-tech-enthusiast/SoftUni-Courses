number_of_lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet_breakage = number_of_lost_fights // 2
total_sword_breakage = number_of_lost_fights // 3
total_shield_breakage = number_of_lost_fights // (2 * 3)
total_armor_breakage = total_shield_breakage // 2

expenses = (total_helmet_breakage * helmet_price
            + total_sword_breakage * sword_price
            + total_shield_breakage * shield_price
            + total_armor_breakage * armor_price)

print(f'Gladiator expenses: {expenses:.2f} aureus')