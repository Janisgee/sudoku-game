import pygame
from pygame.locals import *
from cell import Cell

class Board():
  def __init__(self):
    self._board_size = 630
    self._left_edge = 100
    self._top_edge = 90
    # Store each cell position
    self._cells = []
    for row in range (0,9):
      self._cells.append([])
      for col in range (0,9):
        cell = Cell(self._board_size)
        self._cells[row].append(cell)

  

  def draw_board(self, screen):
    one_third = self._board_size/3
    left = self._left_edge
    right = left + self._board_size
    top = self._top_edge
    bottom = top + self._board_size

    # Draw board square
    pygame.draw.rect(screen, (0,0,0),[left, top, self._board_size,self._board_size],5)

    # Draw board (2 x vertical line & 2 x horizontal line)
    # Vertical Line 1
    pygame.draw.line(screen, (0,0,0), (left + one_third, top),(left + one_third, bottom), 5)
    # Vertical Line 2
    pygame.draw.line(screen, (0,0,0), (left + one_third *2, top),(left + one_third *2, bottom), 5)
    # Horizontal Line 1
    pygame.draw.line(screen, (0,0,0),(left, top + one_third),(right, top + one_third),5)
    # Horizontal Line 2
    pygame.draw.line(screen, (0,0,0),(left, top + one_third *2),(right, top + one_third *2),5)

    # Draw cells
    self.draw_board_cells(screen, top, left)


  def draw_board_cells(self, screen, top, left):
    cell_size = self._board_size/9
    original_left = left

    # Draw Cells
    for row in range (0,9):
      for col in range (0,9):
        self._cells[row][col].draw_cell(screen, top, left)
        left += cell_size
      top += cell_size
      left = original_left