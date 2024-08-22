import pygame
from pygame.locals import *

from .button import Button

class Selection_bar(Button):
  def __init__ (self, screen, text, text_size, button_width, button_height, left_edge, top_edge):
    super().__init__(screen, text, text_size, button_width, button_height, left_edge, top_edge)
    self._menu_data = None

  def selection_bar_event(self, event):
    if event.type == USEREVENT and event.code == "MENU":
      





    





