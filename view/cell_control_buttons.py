import pygame
from pygame.locals import *
from .helper import *

class Cell_control_buttons:
  def __init__ (self, screen, num, button_size, controller, model):
    self._screen = screen
    self._controller = controller
    self._model = model
    self._button_size= button_size
    self._cell_control_num = num
    self._cell_text_size = 60
    self._cell_control_button_fill = (250, 188, 157)
    self._cell_control_button_text_color = (0, 0, 0)
    self._cell_control_button_left = None
    self._cell_control_button_top = None
    self._cell_control_button = None



  def create_cell_control_button(self, top, left):
    screen = self._screen
    button_width = self._button_size
    self._cell_control_button_left = left
    self._cell_control_button_top = top

    # Draw one button
    pygame.draw.rect(screen, self._cell_control_button_fill,[left, top, button_width, button_width])

    # Create button react position
    self._cell_control_button =  pygame.Rect((left, top),(button_width, button_width))

    # Create and display represent number on buttons
    text = f"{self._cell_control_num}"
    display_text_center_at_buttons(self._screen, text, self._cell_control_button_text_color,self._cell_text_size,  button_width,button_width,  top, left,  None, 5)

  def cell_control_button_event(self, event):
    if event.type == pygame.MOUSEMOTION:
      if check_mouse_collision(self._cell_control_button):
        self._cell_control_button_fill = (252, 210, 21)  # Sand yellow
      else:
        self._cell_control_button_fill = (250, 188, 157) # Light orange

    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        if check_mouse_collision(self._cell_control_button):
            self._controller.click_cell_control_number(self._cell_control_num)
          
    
