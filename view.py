
import pygame
from pygame.locals import *
pygame.font.init()
from cell_control_buttons import Cell_control_buttons


# Display View

def display_text_center_at_buttons(screen, text, buttons_size, top, left):
  font = pygame.font.Font(None, 60)
  # Create text
  num_text = font.render(text, True, (0, 0, 128))

  # Get the size of text
  (text_width,text_height) = font.size(text)

  # Display text
  text_left = (left + buttons_size/2) - text_width/2
  text_top = (top + buttons_size/2) - text_height/2+5
  screen.blit(num_text, (text_left, text_top))
    