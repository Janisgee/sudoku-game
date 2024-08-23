
import pygame
from pygame.locals import *
from .button import Button
from .helper import *

class End_game_button(Button):
  def __init__ (self, screen, controller, model, text, text_size, button_width, button_height, left_edge, top_edge):
    super().__init__(screen, controller, model, text, text_size, button_width, button_height, left_edge, top_edge)
    self._model= model
    self._controller = controller


  def button_event(self, event):
    super().button_event(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if check_mouse_collision(self._button):
          self._controller.end_game()
        


          

            
        
    




  

  









    





