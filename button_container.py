import pygame
from pygame.locals import *

from cell_control_buttons import Cell_control_buttons

class Button_container:
  def __init__ (self, screen, board_size):
    self._screen = screen
    self._board_size = board_size
    self._left_edge = 780
    self._top_edge = 90

    # Store each side number control buttons
    self.side_number_buttons=[]
    for i in range (1,10):
      button = Cell_control_buttons(screen,i, self._board_size/9)
      self.side_number_buttons.append(button)


  # Draw side number control buttons
  def draw_side_numbers_buttons(self):
    # draw lines for buttons
    screen = self._screen
    one_nineth = self._board_size/9
    left = self._left_edge
    right = left + one_nineth - 1
    top = self._top_edge

    # Fill button colors and number
    self.fill_side_numbers_buttons()

    # Draw big rectangle for buttons
    pygame.draw.rect(screen, (0,0,0),[left, top, one_nineth, self._board_size],2)

    # Draw vertical lines divides big rectangle into 9 buttons
    for num in range (1,9):
      pygame.draw.line(screen, (0,0,0),(left, top + one_nineth * num),(right, top + one_nineth * num),2)

  def fill_side_numbers_buttons(self):
    # Fill button colors and number
    left = self._left_edge
    top = self._top_edge
    cell_width = self._board_size/9

    for i in range (0, len(self.side_number_buttons)):
      self.side_number_buttons[i].create_cell_control_button(top, left)
      top += cell_width
