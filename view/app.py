import pygame
from pygame.locals import *
import pygame_gui
from .board import Board
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

    # Items for pygame_gui
    self._manager = None
    self._clock = None
    self._time_delta = None

    
  
  def on_init(self):
    # Initialize the pygame library
    pygame.font.init()

    # Set up the drawing window
    self._screen = pygame.display.set_mode((self.width, self.height))
    self.caption = pygame.display.set_caption('Sudoku Game (Created by Janis Chan)')
    # Fill the background with white
    self._screen.fill((255, 255, 255))

    # Setup for pygame gui packager
    self._manager = pygame_gui.UIManager((self.width, self.height))

    # Set font type and size
    self._font1 = pygame.font.SysFont("comicsans",40)
    self._font2 = pygame.font.SysFont("comicsans",20)


    # Create Board
    self._board = Board(self._controller, self._model, self._screen)
    # Create button container for buttons
    self._buttons_group = Buttons_group(self._screen, self._board, self._manager, self._model)
    self._buttons_group.create_all_buttons()

    # Run the App
    self._running = True
    self._clock = pygame.time.Clock()
  
  def on_event(self, event):

    if event.type == pygame.QUIT:
      self._running = False

    # Cell mouse event
    for row in range (0, len(self._board._cells)):
      for col in range (0, len(self._board._cells[row])):
        self._board._cells[row][col].cell_event(event)

    # Game buttons control event
    self._buttons_group.event_from_buttons(event)
  
  def on_render(self):

    # Fill the background with white
    self._screen.fill((255, 255, 255))

    self._board.draw_board()
    # Display game buttons
    self._buttons_group.display_all_buttons()

    self._manager.draw_ui(self._screen)
    
    # Flip the display (Without this line, nothing display)
    pygame.display.flip()


  def on_cleanup(self):
    # Quit game
    pygame.quit()
  
  def on_execute(self):    
    if self.on_init() == False:
      self._running = False
    while (self._running):
      self._time_delta = self._clock.tick(60)/1000.0
      self._manager.update(self._time_delta)

      for event in pygame.event.get():
        self.on_event(event)
        self._manager.process_events(event)

      self.on_render()
    self.on_cleanup()


