from .cell_buttons_control_container import Cell_buttons_control_container
from .game_control_buttons import Game_control_buttons

class Buttons_group:
  def __init__ (self, screen, board, manager):
    self._screen = screen
    self._board = board
    self._manager= manager
    self.cell_buttons_control_container = None
    self.game_control_buttons = None


  def create_all_buttons (self):
    self.cell_buttons_control_container = Cell_buttons_control_container(self._screen, self._board._board_size)
    self.game_control_buttons= Game_control_buttons(self._screen,  self._manager)
    self.game_control_buttons.create_game_control_buttons()

  def display_all_buttons (self):
    # Display side number control event
    self.cell_buttons_control_container.draw_side_numbers_buttons()

    # Display game control buttons
    self.game_control_buttons.draw_game_control_buttons()


  def event_from_buttons(self, event):
    # Side number control event
    for i in range (0, 9):
      self.cell_buttons_control_container.side_number_buttons[i].cell_control_button_event(event)
    
    self.game_control_buttons.game_control_buttons_event(event)