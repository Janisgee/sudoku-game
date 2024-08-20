
import pygame
from pygame.locals import *
pygame.font.init()

from view.view import display_text_center_at_buttons



class Cell():
  def __init__(self, controller, model, screen, board_size, row, col):
    self._controller = controller
    self._model = model
    self._screen = screen
    self._cell_size = board_size / 9
    self._cell_button = None
    self._cell_fill = (240, 240, 240) # grey
    # self._cell_fill_pressed = (211, 238, 240)# red
    self._cell_num_color = (0, 0, 128)
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
    grey = (240, 240, 240)
    red = (211, 238, 240)

    # Change cell color
    if (self.cell_row,self.cell_col) == self._model.selected_cell:
      self._cell_fill = red
    else:
      self._cell_fill = grey
      # Draw one cell
    pygame.draw.rect(screen, self._cell_fill,[left, top, cell_width,cell_width])
    # Create cell react position
    self._cell_button =  pygame.Rect((left, top),(cell_width, cell_width))

    # Display numbers on board
    self.cell_number_display(top, left)
    



  # Set selected cell from controller
  def cell_event(self, event):

    if event.type == pygame.MOUSEBUTTONDOWN:
      # Left click cell and # Right click cell
      if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
        x,y = pygame.mouse.get_pos() # Get click position
        if self._cell_button.collidepoint(x,y): # Check if click is within button, 
          self._controller.click_board_cell((self.cell_row,self.cell_col))
          print(f"{self.cell_row}{self.cell_col}")



  def cell_number_display(self, top, left): 
    cell = self._model.game_list[self.cell_row][self.cell_col]
    # Display " " when list number is 0
    game_num = ""
    if cell == 0:
      game_num = ' '
    else:
      game_num = f'{cell}'
    
    # Create and display text on cell
    display_text_center_at_buttons(self._screen, game_num, self._cell_num_color, self._cell_size, top, left)
