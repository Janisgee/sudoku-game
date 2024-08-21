import pygame
from pygame.locals import *

def check_mouse_collision (button):
  if button:
    x,y = pygame.mouse.get_pos()
    hit = button.collidepoint(x,y)
    if hit:
      return True
    else:
      return False


def check_mouse_left_click(button):
  if pygame.mouse.get_pressed()[0]:
    if check_mouse_collision(button):
      return True
  return False