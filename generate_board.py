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


def helper(board,  row, col):
  if col>8:
    col = 0
    row += 1
  if row >8:
    return board
  
  option_list = find_cell_option(board,row,col)
  while len(option_list) >0:
    # print("option_list",option_list)
    # print("row",row)
    # print("col",col)
    choose_num = random.choice(option_list)
    option_list.remove(choose_num)
    board[row][col] = choose_num
    result = helper(board, row, col+1)
    if result is not None:
      return board
    else:
      board[row][col] = 0
  
  return None
      

def automatic_generate_board():
  row = 0
  col = 0
  board = generate_empty_board()
  result = helper(board, row, col)

  return result
  
  
