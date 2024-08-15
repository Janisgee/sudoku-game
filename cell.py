import pygame
from pygame.locals import *

class Cell():
  def __init__(self, board_size):
    self._cell_size = board_size / 9
    # self._cell_color = (227, 172, 172)

  def draw_cell(self, screen, top, left):
    cell_width = self._cell_size
    # Draw one cell
    pygame.draw.rect(screen, (0,0,0),[left, top, cell_width,cell_width],2)