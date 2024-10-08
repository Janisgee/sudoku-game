
import pygame
from pygame.locals import *
from .button import Button
from .helper import *

class Draft_button(Button):
  def __init__ (self, screen, controller, model, text, text_size, button_width, button_height, left_edge, top_edge, manager):
    super().__init__(screen, controller, model, text, text_size, button_width, button_height, left_edge, top_edge)
    self._model= model
    self._controller = controller
    self._manager = manager
    self.boolean = False

  def button_event(self, event):
    super().button_event(event)
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if check_mouse_collision(self._button):
          
          if self.boolean == False:
            self._text = "Draft: On"
            self.boolean = True
            self._controller.toggle_switch(self.boolean)

          else:
            self._text = "Draft: Off"
            self.boolean = False
            self._controller.toggle_switch(self.boolean)



            
        
    




  

  









    





