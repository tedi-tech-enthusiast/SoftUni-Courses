budget = float(input())
price_of_kg_flour = float(input())

price_of_pack_of_eggs = price_of_kg_flour * 0.75
price_of_milk = (price_of_kg_flour * 1.25) * 0.250

total_cost_per_loaf = price_of_kg_flour + price_of_pack_of_eggs + price_of_milk
count_of_loaves = 0
count_of_colored_eggs = 0

while budget >= total_cost_per_loaf:
    budget -= total_cost_per_loaf
    count_of_loaves += 1
    count_of_colored_eggs += 3

    if count_of_loaves % 3 == 0:
        count_of_colored_eggs -= (count_of_loaves - 2)

print(f"You made {count_of_loaves} loaves of Easter bread! Now you have {count_of_colored_eggs} eggs and {budget:.2f}BGN left.")

