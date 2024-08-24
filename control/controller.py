import copy
import random

class Controller:
  def __init__ (self, model):
    self._game_model = model

  def click_board_cell(self, selected_cell):
    if self._game_model.end_game:
      return 
    row = selected_cell[0]
    col = selected_cell[1]
    game_cell = self._game_model.game_list[row][col]
    if game_cell == 0:
      self._game_model.set_selected_cell(selected_cell)

  def click_cell_control_number(self, num):
    if self._game_model.end_game:
      return 
    cell = self._game_model.selected_cell 
    if cell != None and  self._game_model.player_game_list[cell[0]][cell[1]] == 0:
      # Draft Off
      if self._game_model.draft_button == False:
        self._game_model.player_game_list[cell[0]][cell[1]] = num
        print( self._game_model.player_game_list[cell[0]][cell[1]])
      # Draft On
      else:
        draft_list = self._game_model.all_cell_draft_list[cell[0]][cell[1]]
        if num in draft_list:
          draft_list.remove(num)
        else:
          draft_list.append(num)


  def set_difficulty(self, selected_level):
    self._game_model.selected_level = selected_level

  def toggle_switch (self, boolean):
    self._game_model.draft_button = boolean

  def add_game_time(self, time_delta):
    if self._game_model.end_game == False:  
      self._game_model.total_game_time += time_delta

  def erase_cell_num (self):
    if self._game_model.selected_cell == None:
      return 
    selected_row = self._game_model.selected_cell[0]
    selected_col = self._game_model.selected_cell[1]
    game_num = self._game_model.game_list[selected_row][selected_col]
    player_num = self._game_model.player_game_list[selected_row][selected_col]

    if game_num == 0 and player_num != 0:
      self._game_model.player_game_list[selected_row][selected_col] = 0

  def clear_all_num (self):
    if self._game_model.end_game:
      return
    self._game_model.player_game_list = copy.deepcopy( self._game_model.game_list)
    self._game_model.selected_cell = None

  def show_hint (self):
    if self._game_model.end_game:
      return
    if self._game_model.hint == 0:
      return 
    while True:
      row = random.randrange(0, 9)
      col = random.randrange(0,9)
      if self._game_model.player_game_list[row][col] == 0:
        self._game_model.game_list[row][col] = self._game_model.answer_list[row][col] 
        self._game_model.player_game_list[row][col] = self._game_model.answer_list[row][col] 
        self._game_model.hint-=1
        break

  def end_game(self):
    self._game_model.end_game = True
    self._game_model.selected_cell = None

  def new_game(self):
    self._game_model.set_new_game()


  def number_keypress(self, num):
    self.click_cell_control_number(num)


