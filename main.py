# Install pygame
# graphics class
# logic class
# App class
# main
from debug import *
from generate_board import *

# Function to see the result (progress)
# print("Hardcode Board")
# board = generate_board()
# print_board(board)
#////////////////////////////////////////////
# print("Empty Board")
# board2 = generate_empty_board()
# print_board(board2)

print("Board row")
board3 = automatic_generate_board()
# print_board(board3)

level = {0:("Extremely Easy",32), 1:("Easy",46), 2:("Medium",53), 3:("Difficult",59)}
hidden_list = empty_board_by_difficulty(board3,level[0])
# check_game_board_valid(hidden_list)