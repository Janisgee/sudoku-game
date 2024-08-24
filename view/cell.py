
import pygame
from pygame.locals import *
pygame.font.init()
from .helper import *

class Cell():
  def __init__(self, controller, model, screen, board_size, row, col):
    self._controller = controller
    self._model = model
    self._screen = screen
    self._cell_size = board_size / 9
    self._cell_text_size = 60
    self._cell_button = None
    self._cell_fill = (240, 240, 240) # grey
    self._cell_num_color = (97, 97, 242)
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
    yellow = (252, 210, 21) 
    white = (255,255,255)

    # Change cell color
    if (self.cell_row,self.cell_col) == self._model.selected_cell:
      self._cell_fill = yellow
    else:
      if self._model.game_list[self.cell_row][self.cell_col] == 0:
        self._cell_fill = white
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
      # Left click cell 
      if pygame.mouse.get_pressed()[0]:
        if check_mouse_collision(self._cell_button):
          # If click is within button 
          self._controller.click_board_cell((self.cell_row,self.cell_col))
          print(f"{self.cell_row}{self.cell_col}")


  def cell_number_display(self, top, left): 
    player_cell = self._model.player_game_list[self.cell_row][self.cell_col]
    cell = self._model.game_list[self.cell_row][self.cell_col]
    answer_cell = self._model.answer_list[self.cell_row][self.cell_col]

    # Choose display draft number
    if player_cell == 0 and self._model.end_game == False:
      self.draw_draft_number(top, left)
      return

    # Find display text and color
    display_num = player_cell
    display_color = self._cell_num_color
    display_text = ''

    # Change display num point to answer cell
    if self._model.end_game:
      display_num = answer_cell 
      if player_cell == 0:
        display_color = (255, 187, 0) # Yello - Missing Number
      elif answer_cell == player_cell and cell == 0:
        display_color = (0, 255, 0) # Green - Correct Number
      elif answer_cell != player_cell:
        display_color = (255, 0, 0) # Red - Wrong Number

    elif cell == 0:
      display_color = (0, 0, 0) # Black

    if display_num != 0:
      display_text = f"{display_num}"

    # Create and display text on cell
    display_text_center_at_buttons(self._screen, display_text, display_color, self._cell_text_size, self._cell_size,  self._cell_size, top,  left, None, 5)

  
  def draw_draft_number(self, original_top, original_left):

    one_third = self._cell_size /3
    second_top = original_top + one_third
    third_top = original_top + one_third * 2
    second_left = original_left + one_third
    third_left = original_left + one_third * 2

    for i in self._model.all_cell_draft_list[self.cell_row][self.cell_col]:
      # Display Draft text:
      draft_num = i
      left = original_left
      top = original_top

      if draft_num == 2:
        left = second_left
      if draft_num == 3:
        left = third_left
      if draft_num == 4:
        top = second_top
      if draft_num == 5:
        top = second_top
        left = second_left
      if draft_num == 6:
        top = second_top
        left = third_left
      if draft_num == 7:
        top = third_top
      if draft_num == 8:
        top = third_top
        left = second_left
      if draft_num == 9:
        top = third_top
        left = third_left

      display_color = (163, 163, 162) # grey
      display_text = f"{draft_num}"
    

      # Create and display draft on cell
      display_text_center_at_buttons(self._screen, display_text, display_color, 25, self._cell_size / 3,  self._cell_size / 3, top,  left, None, 3)

  
