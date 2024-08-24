
import pygame
from pygame.locals import *


class Keyboard:
  def __init__ (self, controller):
    self._controller = controller


  def keyboard_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
          self._controller.number_keypress(1)
      if event.key == pygame.K_2:
          self._controller.number_keypress(2)
      if event.key == pygame.K_3:
          self._controller.number_keypress(3)
      if event.key == pygame.K_4:
          self._controller.number_keypress(4)
      if event.key == pygame.K_5:
          self._controller.number_keypress(5)
      if event.key == pygame.K_6:
          self._controller.number_keypress(6)
      if event.key == pygame.K_7:
          self._controller.number_keypress(7)
      if event.key == pygame.K_8:
          self._controller.number_keypress(8)
      if event.key == pygame.K_9:
          self._controller.number_keypress(9)
        
      
        


          

            
        
    




  

  









    





