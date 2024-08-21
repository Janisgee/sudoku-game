import pygame
from pygame.locals import *
from view.view import display_text_center_at_buttons
from .helper import *

class Erase_button:
  def __init__ (self, screen):
    self._screen = screen
    self._erase_button = None
    self._text_color = (0, 0, 0)
    self._text_size = 30
    self._fill_color = (255, 255, 255) #White
    self._button_width = 100
    self._button_heigth = 50
    self._left_edge = 85
    self._top_edge =  205
    self._erase_switch = True
    self._hover = False
    self.create_erase_button(self._left_edge + self._button_width + 10,self._top_edge)

  def draw_button(self):
    screen = self._screen
    erase_left = self._left_edge + self._button_width + 10
    erase_top = self._top_edge

    # Fill color for edit button
    pygame.draw.rect(self._screen, self._fill_color,[erase_left, erase_top, self._button_width, self._button_heigth])

    # Draw rectangle line for edit button and erase
    # Erase button
    pygame.draw.rect(screen, (0,0,0),[erase_left, erase_top, self._button_width ,self._button_heigth ],2)
    self.create_erase_button(erase_left, erase_top)

  def create_erase_button (self, erase_left, erase_top):

    # Create button react position
    self._erase_button = pygame.Rect((erase_left, erase_top),(self._button_width * 2, self._button_heigth))

    # Create text for erase button
    erase_text = f"Erase"

    display_text_center_at_buttons(self._screen, erase_text, self._text_color, self._text_size, self._button_width, self._button_heigth,  erase_top, erase_left, 'Arial')

  def erase_button_event(self, event):
    if hover_button_change_fill_color(event, self._erase_button):
      self._fill_color = (255, 0, 123) # Pink
    else:
      self._fill_color = (255, 255, 255) # White







    





