from .edit_button import Edit_button
from .erase_button import Erase_button

class Game_control_buttons:
  def __init__ (self, screen):
    self._screen = screen
    self._edit_button = None
    self._erase_button = None
  
  def create_game_control_buttons(self):
    # Create edit button and erase button
    self._edit_button = Edit_button(self._screen)
    self._erase_button = Erase_button(self._screen)


  def draw_game_control_buttons(self):
    # Draw edit button and erase button
    self._edit_button.draw_button()
    self._erase_button.draw_button()

  def game_control_buttons_event(self, event):
    self._edit_button.edit_button_event(event)
    self._erase_button.erase_button_event(event)