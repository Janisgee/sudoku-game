import pygame
from pygame.locals import *
from view.view import display_text_center_at_buttons

class Cell_control_buttons:
  def __init__ (self, screen,num, button_size):
    self._screen = screen
    self._button_size= button_size
    self._cell_control_num = num
    self._cell_control_button = None
    self._cell_control_button_fill = (250, 188, 157)
    self._cell_control_button_text_color = (0, 0, 0)
    self._cell_control_button_left = None
    self._cell_control_button_top = None


  def create_cell_control_button(self, top, left):
    screen = self._screen
    button_width = self._button_size
    self._cell_control_button_left = left
    self._cell_control_button_top = top

    # Draw one button
    pygame.draw.rect(screen, self._cell_control_button_fill,[left, top, button_width, button_width])

    # Create button react position
    self._cell_button =  pygame.Rect((left, top),(button_width, button_width))

    # Create and display represent number on buttons
    text = f"{self._cell_control_num}"
    display_text_center_at_buttons(self._screen, text, self._cell_control_button_text_color, button_width, top, left)

  def cell_control_button_event(self, event):
    left = self._cell_control_button_left = left
    top = self._cell_control_button_top
    
    pos = pygame.mouse.get_pos()
    # hit = self.rect.collidepoint(pos)
    print(pos)
