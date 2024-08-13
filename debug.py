
def print_board (board):
  print(f' -----------------------')
  for roll_i in range (len(board)):
    if roll_i == 3 or roll_i == 6:
      print(f' -----------------------')
    print(f'| {board[roll_i][0]},{board[roll_i][1]},{board[roll_i][2]} | {board[roll_i][3]},{board[roll_i][4]},{board[roll_i][5]} | {board[roll_i][6]},{board[roll_i][7]},{board[roll_i][8]} |')

  print(f' -----------------------')