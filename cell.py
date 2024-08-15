import pygame
from pygame.locals import *
pygame.font.init()

class Cell():
  def __init__(self, screen, board_size, row, col):
    self._screen = screen
    self._cell_size = board_size / 9
    self._cell_button = None
    self._cell_fill = (240, 240, 240) # grey
    self.cell_row = row
    self.cell_col = col
    self.cell_left = None
    self.cell_top = None
    self._font = pygame.font.Font(None, 60)
  


  def create_cell(self, top, left):
    screen = self._screen
    cell_width = self._cell_size
    self.cell_left = left
    self.cell_top = top

    # Draw one cell
    pygame.draw.rect(screen, self._cell_fill,[left, top, cell_width,cell_width])
    # Create cell react position
    self._cell_button =  pygame.Rect((left, top),(cell_width, cell_width))

    # Display numbers on board
    self.cell_number_display(top, left)

  def cell_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos() # Get click position
        if self._cell_button.collidepoint(x,y): # Check if click is within button
          print(f"{self.cell_row}{self.cell_col}")
          self._cell_fill = (211, 238, 240) # red
        else:
          self._cell_fill = (240, 240, 240) # grey

  def cell_number_display(self, top, left): 
    # Create text
    num_text = self._font.render(f'{self.cell_row}', True, (0, 0, 128))

    # Get the size of text
    (text_width,text_height) = self._font.size(f'{self.cell_row}')

    # Display text
    text_left = (left + self._cell_size/2) - text_width/2
    text_top = (top + self._cell_size/2) - text_height/2+5
    self._screen.blit(num_text, (text_left, text_top))
    
