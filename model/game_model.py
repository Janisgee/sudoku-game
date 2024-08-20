
from generate_board import automatic_generate_board,empty_board_by_difficulty

class Game_model:
  def __init__(self):
    self.selected_cell= None
    self.answer_list = None
    self.game_list = None
    self.level_list = {0:("Easy",32), 1:("Medium", 46), 2:("Difficult", 50), 3:("Evil", 54)}
    self.selected_level = 0


  def set_new_game(self):
    # Get cell number by automatic generation
    while True:
      self.answer_list = automatic_generate_board()
      level = self.level_list[self.selected_level]
      self.game_list = empty_board_by_difficulty(self.answer_list, level)
      if self.game_list:
        break

  def get_cell_number(self):
    pass

  def set_selected_cell(self, selected_cell):
    self.selected_cell = selected_cell

