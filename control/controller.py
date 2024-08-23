import time

class Controller:
  def __init__ (self, model):
    self._game_model = model
    self.second = 0

  def click_board_cell(self, selected_cell):
    row = selected_cell[0]
    col = selected_cell[1]
    game_cell = self._game_model.game_list[row][col]
    if game_cell == 0:
      self._game_model.set_selected_cell(selected_cell)

  def click_cell_control_number(self, num):
    if self._game_model.draft_button == False:
      cell= self._game_model.selected_cell 
      if self._game_model.selected_cell != None:
        self._game_model.player_game_list[cell[0]][cell[1]] = num
        print(self._game_model.player_game_list[cell[0]][cell[1]])

  def set_difficulty(self, selected_level):
    self._game_model.selected_level = selected_level

  def toggle_switch (self, boolean):
    self._game_model.draft_button = boolean

  def add_game_time(self, time_delta):
    self._game_model.total_game_time += time_delta


