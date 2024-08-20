import pygame
from pygame.locals import *
from cell import Cell

class Board():
  def __init__(self, screen, answer_list, game_list):
    self._screen = screen
    self._board_size = 630
    self._left_edge = 100
    self._top_edge = 90
    # Store each cell position
    self._cells = []
    for row in range (0,9):
      self._cells.append([])
      for col in range (0,9):
        cell_ans = answer_list[row][col]
        cell_num = game_list[row][col]
        cell = Cell(screen, cell_ans, cell_num, self._board_size, row, col)
        self._cells[row].append(cell)


  def draw_board(self):
    screen = self._screen
    one_third = self._board_size/3
    one_nineth = self._board_size/9
    left = self._left_edge
    right = left + self._board_size
    top = self._top_edge
    bottom = top + self._board_size

    # Draw cells
    self.draw_board_cells(top, left)

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


  

  def draw_board_cells(self, top, left):
    cell_size = self._board_size/9
    original_left = left

    # Draw Cells
    for row in range (0,9):
      for col in range (0,9):
        self._cells[row][col].create_cell(top, left)
        left += cell_size
      top += cell_size
      left = original_left