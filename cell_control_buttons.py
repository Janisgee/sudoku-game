import pygame
from pygame.locals import *
from view import display_text_center_at_buttons

class Cell_control_buttons:
  def __init__ (self, screen):
    self._screen = screen
    self._cell_control_button_fill = (230, 230, 230)
    self._cell_control_button_left = None
    self._cell_control_button_top = None


  def create_cell_control_button(self, top, left, num):
    screen = self._screen
    button_width = self._cell_control_button_dimension[0]
    self.cell_left = left
    self.cell_top = top

    # Draw one button
    pygame.draw.rect(screen, self._cell_control_button_fill,[left, top, button_width,button_width])

    # Create button react position
    self._cell_button =  pygame.Rect((left, top),(button_width, button_width))

    # Create and display represent number on buttons
    display_text_center_at_buttons(self._screen, num, button_width, top, left)

