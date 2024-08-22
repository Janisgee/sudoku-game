from .button import Button

class Game_control_buttons:
  def __init__ (self, screen):
    self._screen = screen
    self._selection_bar = None
    self._edit_button = None
    self._erase_button = None
    self._clear_all_button = None
    self._hint_button = None
    self._show_answer_button = None
    self._new_game_button = None
  
  def create_game_control_buttons(self):
    win = self._screen
    text_size = 25
    # First Line Buttons
    # Selection Bar
    self._selection_bar = Button(win, "* Choose Level", text_size, 160, 40, 85, 145 )
    # New Game Button
    self._new_game_button = Button(win, "New Game", text_size, 280, 40, 260, 145 )
    # Timer
    

    # Second Line Buttons
    # Edit Button
    self._edit_button = Button(win, "Edit", text_size, 100, 50, 85, 205)
    # Erase Button
    self._erase_button = Button(win, "Erase", text_size, 100, 50, 190, 205)
    # Clear All Button
    self._clear_all_button = Button (win, "Clear All", text_size, 100, 50, 395, 205)
    # Hint Button
    self._hint_button = Button (win, "Hint", text_size, 100, 50, 500, 205)
    # Show Answer Button
    self._show_answer_button = Button (win, "End Game", text_size, 110, 50, 605, 205)



  def draw_game_control_buttons(self):
    # Draw buttons lines
    self._selection_bar.draw_button()
    self._edit_button.draw_button()
    self._erase_button.draw_button()
    self._clear_all_button.draw_button()
    self._hint_button.draw_button()
    self._show_answer_button.draw_button()
    self._new_game_button.draw_button()

  def game_control_buttons_event(self, event):
    # Hover Event for buttons
    self._selection_bar.button_event(event)
    self._edit_button.button_event(event)
    self._erase_button.button_event(event)
    self._clear_all_button.button_event(event)
    self._hint_button.button_event(event)
    self._show_answer_button.button_event(event)
    self._new_game_button.button_event(event)