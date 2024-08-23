
from pygame.locals import *
from control.controller import Controller
from .button import Button
from .helper import *

class Timer(Button):
  def __init__ (self, screen, model, text, text_size, button_width, button_height, left_edge, top_edge):
    super().__init__(screen, model, text, text_size, button_width, button_height, left_edge, top_edge)

  def create_button(self, left, top):
    second = round(self._model.total_game_time)
    minute = round(second/60)
    second_remain = second % 60
    self._text = f"Timer {minute:02d}:{second_remain:02d}"
    super().create_button(left, top)





    






  

  









    





