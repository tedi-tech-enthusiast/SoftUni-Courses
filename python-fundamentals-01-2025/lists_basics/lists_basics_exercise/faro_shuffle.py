deck_of_cards = input().split()
count_of_shuffles = int(input())

for currant_shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffling = []

    for car_index in range(len(right_part)):
        deck_after_shuffling.append(left_part[car_index])
        deck_after_shuffling.append(right_part[car_index])

    deck_of_cards = deck_after_shuffling.copy()

print(deck_of_cards)