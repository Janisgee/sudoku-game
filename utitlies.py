import pygame
from pygame.locals import *

pygame.font.init()

class Utitlies:
  def __init__ (self):
    self.font1 = None
    self.font2 = None


  def set_font_style(self):
    # Set font type and size
    self._font1 = pygame.font.Font(None,40)
    self._font2 = pygame.font.Font(None,20)