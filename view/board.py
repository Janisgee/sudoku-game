import pygame
from pygame.locals import *
from view.cell import Cell

class Board():
  def __init__(self, controller, model, screen):
    self._controller = controller
    self._model = model
    self._screen = screen
    self._board_size = 630
    self._left_edge = 85
    self._top_edge = 385

    # Store each cell position
    self._cells = []
    for row in range (0,9):
      self._cells.append([])
      for col in range (0,9):
        cell = Cell(controller, model, screen, self._board_size, row, col)
        self._cells[row].append(cell)

  # Draw board lines
  def draw_board(self):
    screen = self._screen
    one_third = self._board_size/3
    one_nineth = self._board_size/9
    left = self._left_edge
    right = left + self._board_size
    top = self._top_edge
    bottom = top + self._board_size

    # Draw cells line
    self.fill_board_cells(top, left)

    # Draw inner-line (8 x vertical line & 8 x horizontal line)
    for num in range (1, 10):
      # vertical inner-line
      pygame.draw.line(screen, (0,0,0), (left + one_nineth * num, top),(left + one_nineth * num, bottom), 1)
      # Horizontal inner-line
      pygame.draw.line(screen, (0,0,0),(left, top + one_nineth * num),(right, top + one_nineth * num),1)

    # Draw board square
    pygame.draw.rect(screen, (0,0,0),[left, top, self._board_size,self._board_size],5)

    # Draw board (2 x vertical line & 2 x horizontal line)
    for num in range (1, 3):
      # Vertical Line 2
      pygame.draw.line(screen, (0,0,0), (left + one_third * num, top),(left + one_third * num, bottom), 5)
      # Horizontal Line 2
      pygame.draw.line(screen, (0,0,0),(left, top + one_third * num),(right, top + one_third * num),5)




  def fill_board_cells(self, top, left):
    cell_size = self._board_size/9
    original_left = left

    # Draw Cells
    for row in range (0,9):
      for col in range (0,9):
        self._cells[row][col].create_cell(top, left)
        left += cell_size
      top += cell_size
      left = original_left