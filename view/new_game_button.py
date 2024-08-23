from .button import Button
from .helper import *

class New_game_button(Button):
  def __init__ (self, screen, model, text, text_size, button_width, button_height, left_edge, top_edge):
    super().__init__(screen, model, text, text_size, button_width, button_height, left_edge, top_edge)
    self._model = model
    self._new_game_button = self._button

  def button_event(self, event):
    super().button_event(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if check_mouse_collision(self._button):
          self._model.set_new_game()
          self._model.total_game_time = 0
  

  









    





