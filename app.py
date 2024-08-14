import pygame
from pygame.locals import *

class App:
  def __init__(self):
    self._running = True
    self._screen = None
    self._caption = None
    self.weight = 1200
    self.height = 800
    self._button_color = (230, 230, 230) # Grey color
    self._button_position = (600, 400) # Centre of screen
    self._button_dimension = (100, 100) # Width and Height
    self._button = pygame.Rect(self._button_position,self._button_dimension )
  
  def on_init(self):
    # Initialize the pygame library
    pygame.init()
    # Set up the drawing window
    self._screen = pygame.display.set_mode([self.weight, self.height])
    self.caption = pygame.display.set_caption('Sudoku Game (Created by Janis Chan)')
    # Fill the background with white
    self._screen.fill((255, 255, 255))
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
  
  def on_loop(self):
    # Draw a Button
    pygame.draw.rect(self._screen, self._button_color, self._button)
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