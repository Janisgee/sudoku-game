import pygame
from pygame.locals import *
from view.view import display_text_center_at_buttons
from .helper import *

class Button:
  def __init__ (self, screen, controller,  model, text, text_size, button_width, button_height, left_edge, top_edge):
    self._screen = screen
    self._controller = controller
    self._model = model
    self._button = None
    self._text = text
    self._text_color = (0, 0, 0)
    self._text_size = text_size
    self._fill_color = (242, 242, 227) #light yellow
    self._button_width = button_width
    self._button_height = button_height
    self._left_edge = left_edge
    self._top_edge =  top_edge
    self.create_button(self._left_edge, self._top_edge)
  

  def draw_button(self):
    screen = self._screen
    left = self._left_edge
    top = self._top_edge

    # Fill color for button
    pygame.draw.rect(self._screen, self._fill_color,[left, top, self._button_width, self._button_height])

    # Draw rectangle line for button
    pygame.draw.rect(screen, (0,0,0),[left, top, self._button_width ,self._button_height ],2)
    self.create_button(left, top)

  def create_button (self, left, top):
    # Create button react position
    self._button = pygame.Rect((left, top),(self._button_width , self._button_height))

    # Create text for button
    text = self._text
    display_text_center_at_buttons(self._screen, text, self._text_color, self._text_size, self._button_width, self._button_height,  top, left, 'Arial')

  def button_event(self, event):
    if event.type == pygame.MOUSEMOTION:
      if check_mouse_collision(self._button):
        self._fill_color = (252, 210, 21) # Sand yellow
      else:
        self._fill_color = (242, 242, 227) #light yellow
    
