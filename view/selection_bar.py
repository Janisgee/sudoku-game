import pygame
from pygame.locals import *
import pygame_gui
from .helper import *
from .button import Button

from control.controller import Controller


class Selection_bar(Button):
  def __init__ (self, screen,model, text, text_size, button_width, button_height, left_edge, top_edge, manager):
    super().__init__(screen, model, text, text_size, button_width, button_height, left_edge, top_edge)
    self._model = model
    self._controller = Controller(model)
    self._manager = manager
    self._menu_data = ["Easy", "Medium", "Difficult", "Evil"]
    self._dropdown = pygame_gui.elements.UIDropDownMenu(self._menu_data, self._menu_data[0], pygame.Rect((self._left_edge, self._top_edge), (self._button_width, self._button_height)),  self._manager)


  def button_event(self, event):
    super().button_event(event)
    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
        if event.ui_element == self._dropdown:
            # Connect selectioin bar to display board with choosen difficulty.
            for key, value in self._model.level_list.items():
              if event.text == value[0]:
                self._controller.set_difficulty(key)

                








    





