
import pygame
from pygame.locals import *
pygame.font.init()



# Display View
def display_text_center_at_buttons(screen, text, text_color, text_size,  buttons_width,buttons_height,  top, left,  text_style = None, align_square_cell=0):
  font = pygame.font.SysFont(text_style, text_size)
  # Create text
  button_text = font.render(text, True, text_color)

  # Get the size of text
  (text_width,text_height) = font.size(text)

  # Display text
  text_left = (left + buttons_width / 2) - text_width/2
  text_top = (top + buttons_height / 2) - text_height/2 + align_square_cell

  screen.blit(button_text, (text_left, text_top))
    

  