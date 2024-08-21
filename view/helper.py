import pygame
from pygame.locals import *

def hover_button_change_fill_color (event, button):
  if event.type == pygame.MOUSEMOTION and button:
    x,y = pygame.mouse.get_pos()
    hit = button.collidepoint(x,y)
    if hit:
      return True
    else:
      return False
