import random
from debug import *
# Function to generate board
def generate_board():
  board = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9],
]
  return board


def generate_empty_board():
  empty_board = []
  for row in range (0, 9):
    row_list = []
    for col in range (0, 9):
        row_list.append(0)  
    empty_board.append(row_list)
  
  return empty_board

def find_cell_option(board, row, col):
  # Return a list of final num options
  options = [1,2,3,4,5,6,7,8,9]

  # Remove the num in the same row
  for num in board[row]:
    if num in options:
      options.remove(num)
  
  # Remove the num in the same col
  for row_i in range (0, len(board)):
    num = board[row_i][col]
    if num in options:
      options.remove(num)
  
  # Remove the num in the same box
  box_row = int(row/3)
  box_col = int(col/3)

  box_first_cell_row = box_row*3
  boc_first_cell_col = box_col*3

  for row_i in range (0,3):
    for col_i in range (0,3):
      num = board[box_first_cell_row+row_i][boc_first_cell_col+col_i]
      if num in options:
        options.remove(num)

  return options



# def automatic_generate_board():
#   board_row = generate_empty_board()
#   row = 0
#   col = 0
#   #Loop each cell
#   while row <9:
#     while col <9:

#       option_list = find_cell_option(board_row,row,col)
#       if len(option_list) > 0:
#         #Random chose from option list
#         choose_num = random.choice(option_list)
#         #Set num in board
#         board_row[row][col]=choose_num
#         col += 1
#       else:
#         if col == 0:
#           col = 8
#           row -= 1
#         else:
#           col -= 1

#     # Set the row and col
#     col = 0 
#     row += 1

#   return board_row


def generate_board_helper(board, row, col, previous_option):
  #Loop each cell
  while row <9:
    while col <9:

      option_list = find_cell_option(board,row,col)
      if len(option_list) > 0:
        #Random chose from option list
        choose_num = random.choice(ele for ele in option_list if ele != previous_option)
        #Set num in board
        board[row][col]=choose_num
        col += 1
      else:
        if col == 0:
          col = 8
          row -= 1
          generate_board_helper(choose_num,row, col)
        else:
          col -= 1
          generate_board_helper(choose_num,row, col)

    # Set the row and col
    col = 0 
    row += 1

    return board

def automatic_generate_board():
  board_row = generate_empty_board()
  new_board = generate_board_helper(board_row, row=0, col=0,  previous_option=None)

  return new_board

