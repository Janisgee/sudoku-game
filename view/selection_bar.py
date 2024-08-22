import pygame
from pygame.locals import *
import pygame_gui
from .helper import *

from .button import Button


class Selection_bar(Button):
  def __init__ (self, screen, text, text_size, button_width, button_height, left_edge, top_edge, manager):
    super().__init__(screen, text, text_size, button_width, button_height, left_edge, top_edge)

    self._manager = manager
    self._menu_data = ["Easy", "Medium", "Difficult", "Evil"]
    self._dropdown = pygame_gui.elements.UIDropDownMenu(self._menu_data, self._menu_data[0], pygame.Rect((self._left_edge, self._top_edge), (self._button_width, self._button_height)),  self._manager)



  def draw_button(self):
    pass

  def selection_bar_event(self, event):

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
        if event.ui_element == self._dropdown:
            print(f'Selected option: {event.text}')


    # if event.type == pygame.MOUSEMOTION:
    #   if check_mouse_collision(self._button):
    #     if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
    #       if event.ui_element == dropdown:
    #         print(f"Selected option: {event.text}")
        





    





