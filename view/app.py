import pygame
from pygame.locals import *
import pygame_gui
from .board import Board
from .buttons_group import Buttons_group
from .keyboard import Keyboard
from .helper import*

class App:
  def __init__(self, controller, model):
    self._controller = controller
    self._model = model
    self._running = True
    self._screen = None
    self._caption = None
    self.width = 800
    self.height = 1100
    self._board = None
    self._buttons_group = None
    self._keyboard = None

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

    # Create Keyboard Listener
    self._keyboard = Keyboard(self._controller)

    # Create Board       
    self._board = Board(self._controller, self._model, self._screen)
    # Create button container for buttons
    self._buttons_group = Buttons_group(self._screen, self._board, self._manager, self._controller, self._model)
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

    # Keyboard control event
    self._keyboard.keyboard_event(event)
  
  def on_render(self):

    # Fill the background with white
    self._screen.fill((255, 255, 255))

    # Display Title "Sudoku"
    font = pygame.font.SysFont("comicsans",60)
    title = font.render("Sudoku", True, (0,0,0))
      # Get the size of text
    (title_width,title_height) = font.size("Sudoku")
    title_left = 800 /2 - title_width / 2

    self._screen.blit(title, (title_left, 40))

    # Display Legend
    if self._model.end_game:
      green = (0, 255, 0) # Correct Number
      yellow = (255, 187, 0) # Missing Number
      red = (255, 0, 0) # Wrong Number
      
      display_text_center_at_buttons(self._screen, "Green = Correct Number", green, 30, 160, 40, 1040, 85)
      display_text_center_at_buttons(self._screen, "Yello = Missing Number", yellow, 30, 160, 40, 1040, 335)
      display_text_center_at_buttons(self._screen, "Red = Wrong Number", red, 30, 160, 40, 1040, 570)
    
    # Display game board
    self._board.draw_board()

    # Display game buttons
    self._buttons_group.display_all_buttons()

    # Display pygame gui stuff
    self._manager.draw_ui(self._screen)

    # self._controller.time_count()
    
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
      self._controller.add_game_time(self._time_delta)
      self._manager.update(self._time_delta)

      for event in pygame.event.get():
        self.on_event(event)
        self._manager.process_events(event)

      self.on_render()
    self.on_cleanup()


