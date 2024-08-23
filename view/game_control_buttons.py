from .button import Button
from .selection_bar import Selection_bar
from .new_game_button import New_game_button
from .draft_button import Draft_button
from .erase_button import Erase_button
from .clear_all_button import Clear_all_button
from .hint_button import Hint_button
from .end_game_button import End_game_button
from .timer import Timer

class Game_control_buttons:
  def __init__ (self, screen,  manager, controller, model):
    self._screen = screen
    self._manager = manager
    self._controller = controller
    self._model = model
    self._selection_bar = None
    self._draft_button = None
    self._erase_button = None
    self._clear_all_button = None
    self._hint_button = None
    self._end_game_button = None
    self._new_game_button = None
    self._timer = None
  
  def create_game_control_buttons(self):
    win = self._screen
    text_size = 25
    # First Line Buttons
    # Selection Bar
    self._selection_bar = Selection_bar(win, self._controller, self._model, "* Choose Level", text_size, 160, 40, 85, 145, self._manager )
    # New Game Button
    self._new_game_button = New_game_button(win, self._controller, self._model, "New Game", text_size, 280, 40, 260, 145 )
    # Timer
    self._timer = Timer(win, self._controller, self._model, "Timer 00:00", text_size, 160, 40, 555, 145)
    

    # Second Line Buttons
    # Draft Button
    self._draft_button = Draft_button(win, self._controller, self._model, "Draft: Off", text_size, 100, 50, 85, 205, self._manager )
    # Erase Button
    self._erase_button = Erase_button(win, self._controller, self._model, "Erase", text_size, 100, 50, 190, 205)
    # Clear All Button
    self._clear_all_button = Clear_all_button (win, self._controller, self._model,"Clear All", text_size, 100, 50, 395, 205)
    # Hint Button
    self._hint_button = Hint_button (win, self._controller, self._model,f"Hint x {self._model.hint}", text_size, 100, 50, 500, 205)
    # Show Answer Button
    self._end_game_button = End_game_button (win, self._controller, self._model,"End Game", text_size, 110, 50, 605, 205)



  def draw_game_control_buttons(self):
    # Draw buttons lines
    self._selection_bar.draw_button()
    self._draft_button.draw_button()
    self._erase_button.draw_button()
    self._clear_all_button.draw_button()
    self._hint_button.draw_button()
    self._end_game_button.draw_button()
    self._new_game_button.draw_button()
    self._timer.draw_button()


  def game_control_buttons_event(self, event):
    # Hover Event for buttons

    self._selection_bar.button_event(event)
    self._draft_button.button_event(event)
    self._erase_button.button_event(event)
    self._clear_all_button.button_event(event)
    self._hint_button.button_event(event)
    self._end_game_button.button_event(event)
    self._new_game_button.button_event(event)

    

