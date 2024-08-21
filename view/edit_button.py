import pygame
from pygame.locals import *
from view.view import display_text_center_at_buttons
from .helper import *

class Edit_button:
  def __init__ (self, screen):
    self._screen = screen
    self._edit_button = None
    self._text_color = (0, 0, 0)
    self._text_size = 30
    self._fill_color = (255, 255, 255) #White
    self._button_width = 100
    self._button_heigth = 50
    self._left_edge = 85
    self._top_edge =  205
    self._erase_switch = "On"
    self.create_edit_button(self._left_edge,self._top_edge)

  def draw_button(self):
    screen = self._screen
    edit_left = self._left_edge
    edit_top = self._top_edge

    # Fill color for edit button
    pygame.draw.rect(self._screen, self._fill_color,[edit_left, edit_top, self._button_width, self._button_heigth])

    # Draw rectangle line for edit button and erase
    # Edit button
    pygame.draw.rect(screen, (0,0,0),[edit_left, edit_top, self._button_width ,self._button_heigth ],2)

    self.create_edit_button(edit_left, edit_top)

  def create_edit_button (self, edit_left, edit_top):
    # Create button react position
    self._edit_button =  pygame.Rect((edit_left, edit_top),(self._button_width, self._button_heigth))

    # Create text for edit button
    edit_text = f"Edit: {self._erase_switch}"

    display_text_center_at_buttons(self._screen, edit_text, self._text_color, self._text_size, self._button_width, self._button_heigth,  edit_top, edit_left, 'Arial')
 

  def edit_button_event(self, event):
    if hover_button_change_fill_color(event, self._edit_button):
      self._fill_color = (255, 0, 123) # Pink
    else:
      self._fill_color = (255, 255, 255) # White







    





