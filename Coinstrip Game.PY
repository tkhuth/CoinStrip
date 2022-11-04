"""
Coin Strip Game
"""
import random
def display_banner():
    print('*' * 15)
    print('COIN STRIP GAME')
    print('*' * 15)
def get_position_number_from_user():
    return int(input('Enter position number of coin: '))
def get_number_places_to_move():
    return int(input('Enter number of places to move coin: '))
def get_next_player_num(player_number):
    if player_number == 1:
        return 2
    return 1
def congratulate_player(player_number):
    print('=' * 29)
    print('** Y O U   H A V E   W O N **')
    print('       PLAYER NUMBER:', player_number)
    print('=' * 29)
def display_coins_list(coins_list):
    coins_list_string = ''.join(coins_list)
    print('123456789')
    print('-' * 9)
    print(coins_list_string)
def check_game_finished(coins_list):
    return coins_list[0:4] == ['$'] * 4
def move_random_character_to_end(coins_list):
    index = random.randrange(0, len(coins_list))
    character = coins_list[index]
    coins_list.pop(index)
    coins_list.append(character)
    return coins_list
def create_coins_list():
    coins_list = ['-', '$', '-', '$', '-', '$', '-', '$', '-']
    for i in range(4):
        coins_list = move_random_character_to_end(coins_list)
    return coins_list
def validate_move(coins_list, position_number, to_move):
    if position_number == 1:
        return False
    elif position_number - to_move < 1:
        return False
    else:
        return coins_list[position_number - to_move - 1: position_number-1] == ['-'] * to_move
def validate_index(coins_list, position_number):
    if position_number in range (1, 10) and coins_list[position_number - 1] == '$':
        return True
    return False
def move_dollar_to_the_left(coins_list, position_number, to_move):
    coins_list[position_number - to_move - 1], coins_list[position_number - 1] = coins_list[position_number - 1], coins_list[position_number - to_move - 1]

def main():
    display_banner()
    play_game()
def play_game():
    player_num = 1
    game_finished = False
    coins_list = create_coins_list()
    while game_finished == False:
        display_coins_list(coins_list)
        print("PLAYER NUMBER: " + str(player_num))
        position_num = get_position_number_from_user()
        if validate_index(coins_list, position_num):
            move_num = get_number_places_to_move()
            if validate_move(coins_list, position_num, move_num):
                move_dollar_to_the_left(coins_list, position_num, move_num)
                game_finished = check_game_finished(coins_list)
                if game_finished:
                     congratulate_player(player_num)
            else:
                print("ERROR: Invalid move!")
        else:
            print("ERROR: Invalid position number!")
        player_num = get_next_player_num(player_num)
main()
