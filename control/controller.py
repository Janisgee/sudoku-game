
from model.game_model import Game_model

class Controller:
  def __init__ (self, model):
    self._game_model = model

  def click_board_cell(self, selected_cell):
    row = selected_cell[0]
    col = selected_cell[1]
    game_cell = self._game_model.game_list[row][col]
    if game_cell == 0:
      self._game_model.set_selected_cell(selected_cell)
      