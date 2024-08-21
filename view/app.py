import pygame
from pygame.locals import *
# from ..control.controller import Controller
# from ..model.game_model import Game_model
from .board import Board
# from .cell_buttons_control_container import Cell_buttons_control_container
from .buttons_group import Buttons_group

class App:
  def __init__(self, controller, model):
    self._controller = controller
    self._model = model
    self._running = True
    self._screen = None
    self._caption = None
    self.width = 800
    self.height = 1100
    self._font1 = None
    self._font2 = None
    self._board = None
    self._buttons_group = None
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


    # Create Board
    self._board = Board(self._controller, self._model, self._screen)
    # Create button container for buttons
    self._buttons_group = Buttons_group(self._screen, self._board)
    self._buttons_group.create_all_buttons()

    # Run the App
    self._running = True

  
  def on_event(self, event):
    if event.type == pygame.QUIT:
      self._running = False


    # Cell mouse event
    for row in range (0, len(self._board._cells)):
      for col in range (0, len(self._board._cells[row])):
        self._board._cells[row][col].cell_event(event)

    # Game buttons control event
    self._buttons_group.event_from_buttons(event)


  
  def on_loop(self):

    self._board.draw_board()
    # Display game buttons
    self._buttons_group.display_all_buttons()
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


