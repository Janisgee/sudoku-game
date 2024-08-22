from .button import Button

class Game_control_buttons:
  def __init__ (self, screen):
    self._screen = screen
    self._edit_button = None
    self._erase_button = None
    self._clear_all_button = None
    self._hint = None
    self._show_answer = None
  
  def create_game_control_buttons(self):
    win = self._screen
    # First Line Buttons

    # Second Line Buttons
    # Edit Button
    self._edit_button = Button(win, "Edit", 30, 100, 50, 85, 205)
    # Erase Button
    self._erase_button = Button(win, "Erase", 30, 100, 50, 190, 205)
    # Clear All Button
    self._clear_all_button = Button (win, "Clear All", 30, 100, 50, 395, 205)
    # Hint Button
    self._hint = Button (win, "Hint", 30, 100, 50, 500, 205)
    # Show Answer Button
    self._show_answer = Button (win, "End Game", 30, 110, 50, 605, 205)



  def draw_game_control_buttons(self):
    # Draw buttons lines
    self._edit_button.draw_button()
    self._erase_button.draw_button()
    self._clear_all_button.draw_button()
    self._hint.draw_button()
    self._show_answer.draw_button()

  def game_control_buttons_event(self, event):
    # Event for buttons
    self._edit_button.button_event(event)
    self._erase_button.button_event(event)
    self._clear_all_button.button_event(event)
    self._hint.button_event(event)
    self._show_answer.button_event(event)