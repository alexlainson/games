from vars_game_board import *

def player_setup():
    player_1_name = input("Name of Player 1: ")
    player_1_colour = input("Blue or Red?: ").lower()
    while True:
        if player_1_colour in ("blue", "red"):
            break
        else:
            player_1_colour = input("Invalid colour. Please select from Blue or Red: ")
    player_2_name = input("Name of Player 2: ")
    if player_1_colour == "blue": 
        player_2_colour = "red"
    else:
        player_2_colour = "blue"
        
    return player_1_name, player_2_name, player_1_colour, player_2_colour


def map_columns():
    column_mapping = {}
    for letter in possible_letters:
        column_mapping[letter] = range(cols)[possible_letters.index(letter)]

    return column_mapping


def colour_assignment(player_colour):
    if player_colour == "blue":
        player_chip = "🔵"
    else:
        player_chip = "🔴"

    return player_chip


def print_game_board():
    print("\n      A    B    C    D    E    F    G  ", end = "")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end = "")
        for y in range(cols):
            if game_board[x][y] == "🔵":
                print("", game_board[x][y], end=" |")
            elif game_board[x][y] == "🔴":
                print("", game_board[x][y], end=" |")
            else:
                print(" ", game_board[x][y], end="  |")
    print("\n   +----+----+----+---------+----+----+")


def modify_board(space_picked, turn):
    game_board[space_picked[0]][space_picked[1]] = turn


def check_for_winner(player_chip, player_name):
    # Horizontal -
    for y in range(rows):
        for x in range(cols - 3):
            if game_board[y][x] == player_chip and game_board[y][x+1] == player_chip and game_board[y][x+2] == player_chip and game_board[y][x+3] == player_chip:
                print("\nGame over!", player_chip, player_name, player_chip, "wins!")
                return True
    # Vertical |
    for y in range(rows - 3):
        for x in range(cols):
            if game_board[y][x] == player_chip and game_board[y+1][x] == player_chip and game_board[y+2][x] == player_chip and game_board[y+3][x] == player_chip:
                print("\nGame over!", player_chip, player_name, player_chip, "wins!")
                return True
    # Diagonal \
    for y in range(rows - 3):
        for x in range(cols - 3):
            if game_board[y][x] == player_chip and game_board[y+1][x+1] == player_chip and game_board[y+2][x+2] == player_chip and game_board[y+3][x+3] == player_chip:
                print("\nGame over!", player_chip, player_name, player_chip, "wins!")
                return True
    # Diagonal /
    for y in range(rows - 3):
        for x in range(3, cols):
            if game_board[y][x] == player_chip and game_board[y+1][x-1] == player_chip and game_board[y+2][x-2] == player_chip and game_board[y+3][x-3] == player_chip:
                print("\nGame over!", player_chip, player_name, player_chip, "wins!")
                return True

    return False


def format_coordinates(input_string):
    column_mapping = map_columns()
    coordinates = [None] * 2
    input_string_upper = input_string.upper()
    if len(input_string_upper) > 2:
        print("Typo?")
    else:
        if input_string_upper[0] in possible_letters and int(input_string_upper[1]) in range(rows):
            coordinates[1] = column_mapping[input_string_upper[0]]
            coordinates[0] = int(input_string_upper[1])
        elif input_string_upper[0] in possible_letters and input_string_upper[1] not in range(rows):
            print("Invalid row")
        elif input_string_upper[0] not in possible_letters and input_string_upper[1] in range(rows):
            print("Invalid column")
        else:
            print("Invalid coordinates")

    return coordinates


def is_space_open(selected_coordinate):
    if game_board[selected_coordinate[0]][selected_coordinate[1]] == "🔵" or game_board[selected_coordinate[0]][selected_coordinate[1]] == "🔴":
        return False
    else:
        return True
    

def drop_check(selected_coordinate):
    coordinate_below = [selected_coordinate[0] + 1, selected_coordinate[1]]
    if selected_coordinate[0] == 5:
        return True
    if is_space_open(coordinate_below) == False:
        return True
    
    return False


def turn(player_colour):
    while True:
        player_chip = colour_assignment(player_colour)
        selected_space = input("\nChoose a space: ")
        coordinate = format_coordinates(selected_space)
        try:
            if(is_space_open(coordinate) is True and drop_check(coordinate) is True):
                modify_board(coordinate, player_chip)
                break
            elif is_space_open(coordinate) == False and drop_check(coordinate) == True:
                print("Space has already been played. Please select another coordinate.")
            elif drop_check(coordinate) == False:
                print("Nowhere for chip to land. Please select another coordinate.")
        except:
            "Error."