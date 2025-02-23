# my_list = [f'A-{number}' for number in range(1,12)]
# print(my_list)
# my_list = [f'B-{number}' for number in range(1,12)]
# print(my_list)
# list comprehension, за да си спестим писането на ръка. Дава ни следния принт:
# ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']


team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

game_is_terminated = False
players = input().split() # input().split(" ")

for player in players:

    if player in team_a:
        team_a.remove(player)

    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_is_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if game_is_terminated: # if game_is_terminated == True
    print('Game was terminated')

