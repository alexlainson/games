from vars_game_board import *
from vars_players import *
from helper_functions import *

print("\nWelcome to Connect4!")
print("\nMatch:", player_1_name, "vs.", player_2_name)

print_game_board()

turn_counter = 0
while True:
    if turn_counter % 2 == 0:
        turn(player_1_colour)
        winner = check_for_winner(colour_assignment(player_1_colour), player_1_name)
        turn_counter += 1
        print_game_board()
    else:
        turn(player_2_colour)
        winner = check_for_winner(colour_assignment(player_2_colour), player_2_name)
        turn_counter += 1
        print_game_board()

    if winner:
        break