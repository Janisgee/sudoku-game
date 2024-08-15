import pygame
from pygame.locals import *

class Cell():
  def __init__(self, board_size, row, col):
    self._cell_size = board_size / 9
    self._cell_button = None
    self._cell_fill = (230, 230, 230)
    self.cell_row = row
    self.cell_col = col

  def create_cell(self, screen, top, left):
    cell_width = self._cell_size
    # Draw one cell
    pygame.draw.rect(screen, self._cell_fill,[left, top, cell_width,cell_width])
    # Create cell react position
    self._cell_button =  pygame.Rect((left, top),(cell_width, cell_width))

  def cell_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos() # Get click position
        if self._cell_button.collidepoint(x,y): # Check if click is within button
          print(f"{self.cell_row}{self.cell_col}")
          self._cell_color = (237, 45, 45)