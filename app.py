import pygame
from pygame.locals import *
from board import Board
from generate_board import automatic_generate_board,empty_board_by_difficulty
from button_container import Button_container

class App:
  def __init__(self):
    self._running = True
    self._screen = None
    self._caption = None
    self.width = 1200
    self.height = 800
    self._button_color = (230, 230, 230) # Grey color
    self._button_position = (600, 400) # Centre of screen
    self._button_dimension = (100, 100) # Width and Height
    self._button = pygame.Rect(self._button_position,self._button_dimension )
    self._font1 = None
    self._font2 = None
    self._board = None
    self._button_container = None
    self._level = {0:("Easy",32), 1:("Medium", 46), 2:("Difficult", 50), 3:("Evil", 54)}

    
  
  def on_init(self):
    # Initialize the pygame library
    pygame.font.init()

    # Set up the drawing window
    self._screen = pygame.display.set_mode((self.width, self.height))
    self.caption = pygame.display.set_caption('Sudoku Game (Created by Janis Chan)')
    # Fill the background with white
    self._screen.fill((255, 255, 255))

    # Set font type and size
    self._font1 = pygame.font.SysFont("comicsans",40)
    self._font2 = pygame.font.SysFont("comicsans",20)


    # Get cell number by automatic generation
    while True:
      answer_list = automatic_generate_board()
      level = self._level[0]
      game_list = empty_board_by_difficulty(answer_list, level)
      if game_list:
        break

    # Create Board
    self._board = Board(self._screen, answer_list, game_list)
    # Create button container for buttons
    self._button_container = Button_container(self._screen, self._board._board_size)

    # Run the App
    self._running = True



   
  
  def on_event(self, event):
    if event.type == pygame.QUIT:
      self._running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos() # Get click position
        if self._button.collidepoint(x,y): # Check if click is within button
          print("Mouse button pressed!")
          self._button_color = (237, 45, 45)

    # Cell mouse event
    for row in range (0, len(self._board._cells)):
      for col in range (0, len(self._board._cells[row])):
        self._board._cells[row][col].cell_event(event)

  
  def on_loop(self):
    # Draw a Button
    pygame.draw.rect(self._screen, self._button_color, self._button)
 
    self._board.draw_board()
    self._button_container.draw_side_numbers_buttons()
    pygame.display.update()
  
  def on_render(self):
    
    # Flip the display (Without this line, nothing display)
    pygame.display.flip()

    

  def on_cleanup(self):
    # Quit game
    pygame.quit()
  
  def on_execute(self):
    if self.on_init() == False:
      self._running = False

    while (self._running):
      for event in pygame.event.get():
        self.on_event(event)

      self.on_loop()
      self.on_render()
    self.on_cleanup()


if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()